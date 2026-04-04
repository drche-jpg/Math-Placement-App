import streamlit as st
import gspread
import datetime
import pandas as pd
import plotly.express as px
import random
from questions import all_questions

# --- 1. CORE FUNCTIONS & GSHEETS ---
def init_gsheets():
    """เชื่อมต่อและจัดการหัวตารางใน Google Sheets"""
    try:
        if "gcp_service_account" in st.secrets:
            creds_dict = dict(st.secrets["gcp_service_account"])
            client = gspread.service_account_from_dict(creds_dict)
            sh = client.open("Math_Placement_Results").sheet1
            
            # สร้าง Header ถ้า Sheet ยังว่างอยู่
            if not sh.get('A1'):
                headers = ["Timestamp", "Student Name", "Difficulty", "Total Score", "Percentage", "Teacher Feedback"]
                # เพิ่มหัวตารางรายข้อ Q1_Ans, Q1_Status, Q2_Ans, Q2_Result...
                for i in range(1, 21):
                    headers.extend([f"Q{i}_Ans", f"Q{i}_Status"])
                sh.append_row(headers)
            return sh
    except Exception as e:
        st.error(f"Spreadsheet connection failed: {e}")
    return None

# --- 2. CONFIGURATION ---
st.set_page_config(page_title="Math Olympiad Placement", layout="wide")

for key in ['page', 'student_name', 'difficulty', 'user_answers', 'selected_quiz']:
    if key not in st.session_state:
        st.session_state[key] = "setup" if key == 'page' else "" if key != 'selected_quiz' else []

# --- 3. PAGE LOGIC ---

# PAGE 1: SETUP
if st.session_state.page == "setup":
    st.title("🏆 Mathematics Competition Placement")
    st.markdown("### Talent Search & Diagnostic Assessment (Grade 7-9)")
    
    with st.form("setup_form"):
        name = st.text_input("Candidate Full Name (ชื่อ-นามสกุล):")
        level = st.selectbox("Select Exam Difficulty:", ["Level 1: Easy", "Level 2: Intermediate", "Level 3: Difficult"])
        
        if st.form_submit_button("Initialize Examination"):
            if name:
                level_qs = [q for q in all_questions if q['difficulty'] == level]
                # สุ่มข้อสอบ 20 ข้อ
                selected = random.sample(level_qs, min(20, len(level_qs)))
                # สุ่มลำดับตัวเลือก A, B, C, D ของแต่ละข้อ
                for item in selected:
                    random.shuffle(item['options'])
                    
                st.session_state.selected_quiz = selected
                st.session_state.update({"student_name": name, "difficulty": level, "page": "quiz", "user_answers": {}})
                st.rerun()
            else:
                st.warning("กรุณากรอกชื่อนักเรียนก่อนเริ่มทำข้อสอบ")

# PAGE 2: QUIZ
elif st.session_state.page == "quiz":
    st.title(f"Assessment: {st.session_state.difficulty}")
    st.info(f"Student: **{st.session_state.student_name}** | Exam in Progress...")
    
    with st.form("quiz_form"):
        temp_answers = {}
        for idx, q in enumerate(st.session_state.selected_quiz):
            st.markdown(f"#### Problem {idx+1}")
            st.markdown(f"**{q['question']}**")
            
            if "image_svg" in q:
                st.markdown(q["image_svg"], unsafe_allow_html=True)
            
            # แสดง Choice เหนือปุ่มกด
            st.markdown(f"**A)** {q['options'][0]} &nbsp;&nbsp;&nbsp; **B)** {q['options'][1]} &nbsp;&nbsp;&nbsp; **C)** {q['options'][2]} &nbsp;&nbsp;&nbsp; **D)** {q['options'][3]}")
            
            choice = st.radio("Selection:", ["A", "B", "C", "D"], key=q['id'], index=None, horizontal=True)
            
            l_map = {"A": q['options'][0], "B": q['options'][1], "C": q['options'][2], "D": q['options'][3]}
            temp_answers[q['id']] = l_map.get(choice)
            st.divider()
            
        if st.form_submit_button("Submit Final Script"):
            st.session_state.user_answers = temp_answers
            st.session_state.page = "results"
            st.rerun()

# PAGE 3: RESULTS & DETAILED LOGGING
elif st.session_state.page == "results":
    st.header(f"Performance Analysis: {st.session_state.student_name}")
    
    # คำนวณคะแนน
    score = 0
    detailed_results_for_sheet = [] # เก็บ Ans และ Status เพื่อเซฟลง Sheet
    
    for q in st.session_state.selected_quiz:
        u_ans = st.session_state.user_answers.get(q['id'], "No Answer")
        is_correct = (u_ans == q['answer'])
        if is_correct: score += 1
        
        # เก็บข้อมูลรายข้อ [คำตอบที่เลือก, สถานะ]
        detailed_results_for_sheet.extend([u_ans, "Correct" if is_correct else "Incorrect"])

    perc = (score / 20) * 100
    
    # แสดงผลเบื้องต้น
    col1, col2 = st.columns([1, 1])
    with col1:
        st.metric("Total Score", f"{score}/20", f"{perc:.0f}%")
        # สร้าง Radar Chart (เหมือนเดิม)
        # ... (โค้ด Radar Chart)
        
    with col2:
        st.subheader("Pedagogical Feedback")
        if perc >= 85:
            feedback = "Exceptional performance! Advanced mastery of logical deduction."
        elif perc >= 60:
            feedback = "Solid foundation. Some minor inconsistencies in execution."
        else:
            feedback = "Diagnostic complete. Strengthening foundational principles is recommended."
        st.write(feedback)

    # --- ส่วนการเซฟข้อมูลแบบละเอียดลง Google Sheet ---
    sheet = init_gsheets()
    if sheet:
        try:
            ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # ข้อมูลพื้นฐาน + ข้อมูลรายข้อ (Ans/Status) ทั้งหมด
            row_to_add = [ts, st.session_state.student_name, st.session_state.difficulty, score, f"{perc:.0f}%", feedback] + detailed_results_for_sheet
            sheet.append_row(row_to_add)
            st.success("Full analysis and detailed answers archived successfully.")
        except:
            st.warning("Could not sync detailed answers to the cloud.")

    # --- ส่วนการตรวจคำตอบรายข้อ (Show Answers) ---
    st.divider()
    st.subheader("📝 Detailed Answer Review")
    for idx, q in enumerate(st.session_state.selected_quiz):
        u_ans = st.session_state.user_answers.get(q['id'])
        correct = (u_ans == q['answer'])
        
        with st.expander(f"Problem {idx+1}: {'✅' if correct else '❌'}", expanded=not correct):
            st.write(f"**Q:** {q['question']}")
            if "image_svg" in q: st.markdown(q["image_svg"], unsafe_allow_html=True)
            st.write(f"**Your Answer:** {u_ans}")
            st.success(f"**Correct Answer:** {q['answer']}")
            st.info(f"**Logic:** {q['solution']}")

    if st.button("Start New Session"):
        st.session_state.page = "setup"
        st.rerun()
