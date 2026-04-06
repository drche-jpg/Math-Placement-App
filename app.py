import streamlit as st
import gspread
import datetime
import pandas as pd
import plotly.express as px
import random
from questions import all_questions

# --- 1. ฟังก์ชันจัดการ Google Sheets พร้อมระบบ Auto-Header ---
def init_gsheets():
    """เชื่อมต่อ Google Sheets และสร้างหัวตารางแบบละเอียด"""
    try:
        if "gcp_service_account" in st.secrets:
            creds_dict = dict(st.secrets["gcp_service_account"])
            client = gspread.service_account_from_dict(creds_dict)
            sh = client.open("Math_Placement_Results").sheet1
            
            # ถ้าช่อง A1 ว่าง ให้สร้าง Headers ใหม่
            if not sh.get('A1'):
                # ส่วนที่ 1: ข้อมูลสรุปและผลการประเมิน
                headers = [
                    "Timestamp", "Student Name", "Difficulty Level", 
                    "Total Score (20)", "Percentage (%)", "Teacher's Evaluation"
                ]
                
                # ส่วนที่ 2: ข้อมูลสำหรับ Radar Chart (คะแนนรายหมวดหมู่ %)
                headers.extend([
                    "Number Sense (%)", "Algebra (%)", "Geometry (%)", "Probability (%)"
                ])
                
                # ส่วนที่ 3: รายละเอียดคำตอบรายข้อ (Q1-Q20)
                for i in range(1, 21):
                    headers.append(f"Q{i}_Student_Ans")
                    headers.append(f"Q{i}_Result")
                
                sh.append_row(headers)
            return sh
    except Exception as e:
        st.error(f"การเชื่อมต่อฐานข้อมูลขัดข้อง: {e}")
    return None
# โค้ดสำหรับซ่อนเมนู มุมขวาบน และ Footer ของ Streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# --- 2. CONFIGURATION ---
st.set_page_config(page_title="Math Olympiad Placement", layout="wide")

for key in ['page', 'student_name', 'difficulty', 'user_answers', 'selected_quiz']:
    if key not in st.session_state:
        st.session_state[key] = "setup" if key == 'page' else "" if key != 'selected_quiz' else []

# --- 3. PAGE ROUTING ---

# หน้าที่ 1: ตั้งค่าผู้สอบ
if st.session_state.page == "setup":
    st.title("🏆 Mathematics Competition Placement Exam")
    st.markdown("### Talent Search & Diagnostic Assessment")
    
    with st.form("setup_form"):
        name = st.text_input("Candidate Full Name (ชื่อ-นามสกุล):")
        level = st.selectbox("Select Difficulty Level:", ["Level 1: Easy", "Level 2: Intermediate", "Level 3: Difficult"])
        if st.form_submit_button("Initialize Examination"):
            if name:
                level_qs = [q for q in all_questions if q['difficulty'] == level]
                selected = random.sample(level_qs, min(20, len(level_qs)))
                for item in selected:
                    random.shuffle(item['options'])
                st.session_state.selected_quiz = selected
                st.session_state.update({"student_name": name, "difficulty": level, "page": "quiz", "user_answers": {}})
                st.rerun()
            else:
                st.warning("กรุณากรอกชื่อนักเรียนก่อนเริ่มทำข้อสอบ")

# หน้าที่ 2: หน้าทำข้อสอบ
elif st.session_state.page == "quiz":
    st.title(f"Assessment: {st.session_state.difficulty}")
    st.info(f"Student: **{st.session_state.student_name}**")
    
    with st.form("quiz_form"):
        temp_answers = {}
        for idx, q in enumerate(st.session_state.selected_quiz):
            st.markdown(f"#### Problem {idx+1}")
            st.markdown(f"**{q['question']}**")
            if "image_svg" in q:
                st.markdown(q["image_svg"], unsafe_allow_html=True)
            st.markdown(f"**A)** {q['options'][0]} &nbsp;&nbsp;&nbsp; **B)** {q['options'][1]} &nbsp;&nbsp;&nbsp; **C)** {q['options'][2]} &nbsp;&nbsp;&nbsp; **D)** {q['options'][3]}")
            choice = st.radio("Selection:", ["A", "B", "C", "D"], key=q['id'], index=None, horizontal=True)
            l_map = {"A": q['options'][0], "B": q['options'][1], "C": q['options'][2], "D": q['options'][3]}
            temp_answers[q['id']] = l_map.get(choice)
            st.divider()
        if st.form_submit_button("Submit Final Script"):
            st.session_state.user_answers = temp_answers
            st.session_state.page = "results"
            st.rerun()

# หน้าที่ 3: หน้าสรุปผลและการบันทึกข้อมูล (อัปเดต Radar Data)
elif st.session_state.page == "results":
    st.header(f"Performance Analysis: {st.session_state.student_name}")
    
    score = 0
    categories = ["Number Sense & Operations", "Pre-Algebra & Equations", "Geometry & Data", "Number Theory & Probability"]
    cat_stats = {c: {"c": 0, "t": 0} for c in categories}
    detailed_data_for_sheet = [] 
    
    for q in st.session_state.selected_quiz:
        cat = q['category']
        cat_stats[cat]["t"] += 1
        user_ans = st.session_state.user_answers.get(q['id'])
        is_correct = (user_ans == q['answer'])
        if is_correct:
            score += 1
            cat_stats[cat]["c"] += 1
        detailed_data_for_sheet.extend([user_ans if user_ans else "No Answer", "Correct" if is_correct else "Incorrect"])

    perc = (score / 20) * 100
    
    # คำนวณคะแนนรายหมวดหมู่สำหรับ Radar Chart และการเซฟข้อมูล
    radar_scores = []
    for c in categories:
        val = (cat_stats[c]['c'] / cat_stats[c]['t'] * 100) if cat_stats[c]['t'] > 0 else 0
        radar_scores.append(f"{val:.0f}%")

    col1, col2 = st.columns([1, 1])
    with col1:
        st.metric("Final Score", f"{score}/20", f"{perc:.0f}%")
        radar_df = pd.DataFrame([{"Category": k, "Score": (v['c']/v['t'])*100 if v['t']>0 else 0} for k,v in cat_stats.items()])
        fig = px.line_polar(radar_df, r='Score', theta='Category', line_close=True, range_r=[0,100])
        fig.update_traces(fill='toself', line_color='#FF4B4B')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Pedagogical Evaluation")
        if perc >= 85: feedback = "Exceptional performance! Ready for advanced Olympiad training."
        elif perc >= 60: feedback = "Solid foundation. Focus on speed and complex execution."
        else: feedback = "Diagnostic complete. Reinforcing basic principles is recommended."
        st.write(feedback)

    # 3. บันทึกลง Google Sheet (ครบทุกมิติ)
    sheet = init_gsheets()
    if sheet:
        try:
            ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # [ข้อมูลพื้นฐาน] + [คะแนน Radar 4 หมวด] + [ผลรายข้อ 20 ข้อ]
            final_row = [ts, st.session_state.student_name, st.session_state.difficulty, score, f"{perc:.0f}%", feedback] + radar_scores + detailed_data_for_sheet
            sheet.append_row(final_row)
            st.success("Analysis, Evaluation, Radar Data, and Detailed Answers archived successfully.")
        except:
            st.warning("Database sync failed.")

    # 4. Review
    with st.expander("📝 Detailed Answer Review"):
        for idx, q in enumerate(st.session_state.selected_quiz):
            u_ans = st.session_state.user_answers.get(q['id'])
            correct = (u_ans == q['answer'])
            st.write(f"**Problem {idx+1}: {'✅' if correct else '❌'}**")
            st.write(f"Question: {q['question']}")
            st.success(f"Correct Answer: {q['answer']}")
            st.info(f"Logic: {q['solution']}")

    if st.button("New Examination Session"):
        for k in ['student_name', 'difficulty', 'user_answers', 'selected_quiz']:
            st.session_state[k] = "" if k != 'selected_quiz' else []
        st.session_state.page = "setup"
        st.rerun()
