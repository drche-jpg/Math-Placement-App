import streamlit as st
import gspread
import datetime
import pandas as pd
import plotly.express as px
import random
from questions import all_questions

# --- 1. ฟังก์ชันจัดการ Google Sheets พร้อมระบบ Auto-Header ---
def init_gsheets():
    """เชื่อมต่อ Google Sheets และสร้างหัวตารางถ้ายังไม่มี"""
    try:
        if "gcp_service_account" in st.secrets:
            creds_dict = dict(st.secrets["gcp_service_account"])
            client = gspread.service_account_from_dict(creds_dict)
            sh = client.open("Math_Placement_Results").sheet1
            
            # ตรวจสอบว่าช่อง A1 ว่างหรือไม่ ถ้าว่างให้ใส่หัวกระดาษ (Headers)
            if not sh.get('A1'):
                # ส่วนที่ 1: ข้อมูลสรุป
                headers = [
                    "Timestamp", 
                    "Student Name", 
                    "Difficulty Level", 
                    "Total Score (out of 20)", 
                    "Percentage (%)", 
                    "Teacher's Evaluation"
                ]
                
                # ส่วนที่ 2: รายละเอียดรายข้อ (Q1 ถึง Q20)
                for i in range(1, 21):
                    headers.append(f"Q{i}_Student_Ans")
                    headers.append(f"Q{i}_Result")
                
                sh.append_row(headers)
            return sh
    except Exception as e:
        st.error(f"การเชื่อมต่อฐานข้อมูลขัดข้อง: {e}")
    return None

# --- 2. การตั้งค่าหน้าจอและ SESSION STATE ---
st.set_page_config(page_title="Math Olympiad Placement", layout="wide")

for key in ['page', 'student_name', 'difficulty', 'user_answers', 'selected_quiz']:
    if key not in st.session_state:
        st.session_state[key] = "setup" if key == 'page' else "" if key != 'selected_quiz' else []

# --- 3. ตรรกะการเปลี่ยนหน้า (PAGE ROUTING) ---

# --- หน้าที่ 1: ตั้งค่าผู้สอบ ---
if st.session_state.page == "setup":
    st.title("🏆 Mathematics Competition Placement Exam")
    st.markdown("### Talent Search & Diagnostic Assessment (Grade 7-9)")
    
    with st.form("setup_form"):
        name = st.text_input("Candidate Full Name (ชื่อ-นามสกุล):")
        level = st.selectbox("Select Difficulty Level:", ["Level 1: Easy", "Level 2: Intermediate", "Level 3: Difficult"])
        
        if st.form_submit_button("Initialize Examination"):
            if name:
                # กรองโจทย์ตามระดับความยาก
                level_qs = [q for q in all_questions if q['difficulty'] == level]
                # สุ่มข้อสอบ 20 ข้อ
                selected = random.sample(level_qs, min(20, len(level_qs)))
                
                # สุ่มลำดับตัวเลือก (A, B, C, D) ของแต่ละข้อให้แตกต่างกันทุกครั้ง
                for item in selected:
                    random.shuffle(item['options'])
                    
                st.session_state.selected_quiz = selected
                st.session_state.update({"student_name": name, "difficulty": level, "page": "quiz", "user_answers": {}})
                st.rerun()
            else:
                st.warning("กรุณากรอกชื่อนักเรียนก่อนเริ่มทำข้อสอบ")

# --- หน้าที่ 2: หน้าทำข้อสอบ ---
elif st.session_state.page == "quiz":
    st.title(f"Assessment: {st.session_state.difficulty}")
    st.info(f"Student: **{st.session_state.student_name}** | Exam in Progress...")
    
    with st.form("quiz_form"):
        temp_answers = {}
        for idx, q in enumerate(st.session_state.selected_quiz):
            st.markdown(f"#### Problem {idx+1}")
            st.markdown(f"**{q['question']}**")
            
            # แสดงรูปภาพ (SVG) ถ้ามี
            if "image_svg" in q:
                st.markdown(q["image_svg"], unsafe_allow_html=True)
            
            # แสดงตัวเลือกข้อความ (A, B, C, D)
            st.markdown(f"**A)** {q['options'][0]} &nbsp;&nbsp;&nbsp; **B)** {q['options'][1]} &nbsp;&nbsp;&nbsp; **C)** {q['options'][2]} &nbsp;&nbsp;&nbsp; **D)** {q['options'][3]}")
            
            choice = st.radio("Selection:", ["A", "B", "C", "D"], key=q['id'], index=None, horizontal=True)
            
            # เก็บคำตอบที่เลือก (เก็บเป็นตัวหนังสือ)
            l_map = {"A": q['options'][0], "B": q['options'][1], "C": q['options'][2], "D": q['options'][3]}
            temp_answers[q['id']] = l_map.get(choice)
            st.divider()
            
        if st.form_submit_button("Submit Final Script"):
            st.session_state.user_answers = temp_answers
            st.session_state.page = "results"
            st.rerun()

# --- หน้าที่ 3: หน้าสรุปผลและการบันทึกข้อมูล ---
elif st.session_state.page == "results":
    st.header(f"Performance Analysis: {st.session_state.student_name}")
    
    # 1. คำนวณคะแนนรวมและคะแนนรายวิชา
    score = 0
    categories = ["Number Sense & Operations", "Pre-Algebra & Equations", "Geometry & Data", "Number Theory & Probability"]
    cat_stats = {c: {"c": 0, "t": 0} for c in categories}
    detailed_data_for_sheet = [] # สำหรับเซฟ Ans/Result ลง Sheet
    
    for q in st.session_state.selected_quiz:
        cat = q['category']
        cat_stats[cat]["t"] += 1
        user_ans = st.session_state.user_answers.get(q['id'])
        is_correct = (user_ans == q['answer'])
        
        if is_correct:
            score += 1
            cat_stats[cat]["c"] += 1
            
        # เก็บคำตอบรายข้อเพื่อส่งเข้า Google Sheet
        detailed_data_for_sheet.extend([user_ans if user_ans else "No Answer", "Correct" if is_correct else "Incorrect"])

    perc = (score / 20) * 100
    
    # 2. แสดงผลบนหน้าจอ
    col1, col2 = st.columns([1, 1])
    with col1:
        st.metric("Final Score", f"{score}/20", f"{perc:.0f}%")
        # สร้าง Radar Chart
        radar_df = pd.DataFrame([{"Category": k, "Score": (v['c']/v['t'])*100 if v['t']>0 else 0} for k,v in cat_stats.items()])
        fig = px.line_polar(radar_df, r='Score', theta='Category', line_close=True, range_r=[0,100])
        fig.update_traces(fill='toself', line_color='#FF4B4B')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Pedagogical Evaluation")
        if perc >= 85:
            feedback = f"Excellent! {st.session_state.student_name} displays exceptional mastery in {st.session_state.difficulty}. Ready for advanced training."
        elif perc >= 60:
            feedback = f"Solid foundation. {st.session_state.student_name} shows competence but needs focus on complex execution."
        else:
            feedback = f"Diagnostic complete. {st.session_state.student_name} would benefit from reinforcing foundational principles."
        st.write(feedback)
        st.info(f"**Growth Focus:** Strengthen skills in '{radar_df.sort_values('Score').iloc[0]['Category']}'")

    # 3. บันทึกลง Google Sheet พร้อมหัวตารางละเอียด
    sheet = init_gsheets()
    if sheet:
        try:
            ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            base_info = [ts, st.session_state.student_name, st.session_state.difficulty, score, f"{perc:.0f}%", feedback]
            final_row = base_info + detailed_data_for_sheet
            sheet.append_row(final_row)
            st.success("Analysis and detailed student answers archived successfully.")
        except:
            st.warning("Database sync failed; results displayed on-screen only.")

    # 4. แสดงเฉลยละเอียดรายข้อ
    st.divider()
    st.subheader("📝 Detailed Answer Review")
    for idx, q in enumerate(st.session_state.selected_quiz):
        u_ans = st.session_state.user_answers.get(q['id'])
        correct = (u_ans == q['answer'])
        with st.expander(f"Problem {idx+1}: {'✅' if correct else '❌'}", expanded=not correct):
            st.markdown(f"**Question:** {q['question']}")
            if "image_svg" in q:
                st.markdown(q["image_svg"], unsafe_allow_html=True)
            st.write(f"**Your Answer:** {u_ans}")
            st.success(f"**Correct Answer:** {q['answer']}")
            st.info(f"**Logic:** {q['solution']}")

    if st.button("New Examination Session"):
        for k in ['student_name', 'difficulty', 'user_answers', 'selected_quiz']:
            st.session_state[k] = "" if k != 'selected_quiz' else []
        st.session_state.page = "setup"
        st.rerun()
