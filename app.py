import streamlit as st
import gspread
import datetime
import pandas as pd
import plotly.express as px
import random
# -> NEW: Import the question bank from your other file
from questions import all_questions 

# --- 1. GOOGLE SHEETS SETUP ---
def init_gsheets():
    if "gcp_service_account" in st.secrets:
        creds_dict = dict(st.secrets["gcp_service_account"])
        client = gspread.service_account_from_dict(creds_dict)
    else:
        client = gspread.service_account(filename='credentials.json')
        
    sheet = client.open("Math_Placement_Results").sheet1
    return sheet

# --- 2. UI, ROUTING AND LOGIC ---
st.set_page_config(page_title="Math Placement Test", layout="centered")

if 'page' not in st.session_state:
    st.session_state.page = "setup"
if 'student_name' not in st.session_state:
    st.session_state.student_name = ""
if 'difficulty' not in st.session_state:
    st.session_state.difficulty = ""
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}
# -> NEW: Track which random questions were selected for this student
if 'selected_quiz' not in st.session_state:
    st.session_state.selected_quiz = []

# ==========================================
# PAGE 1: SETUP AND DIFFICULTY SELECTION
# ==========================================
if st.session_state.page == "setup":
    st.title("Welcome to the Math Placement Test")
    st.markdown("Please enter your details and select your assigned test difficulty.")
    
    with st.form("setup_form"):
        name = st.text_input("Student Name:")
        level = st.selectbox(
            "Select Difficulty Level:", 
            ["Level 1: Easy", "Level 2: Intermediate", "Level 3: Difficult"]
        )
        
        start_btn = st.form_submit_button("Start Test")
        
        if start_btn:
            if not name:
                st.error("Please enter your name to begin.")
            else:
                st.session_state.student_name = name
                st.session_state.difficulty = level
                
                # -> NEW: Pull questions matching the difficulty and randomly select 20
                level_questions = [q for q in all_questions if q['difficulty'] == level]
                st.session_state.selected_quiz = random.sample(level_questions, min(20, len(level_questions)))
                
                st.session_state.page = "quiz"
                st.rerun()

# ==========================================
# PAGE 2: THE QUIZ
# ==========================================
elif st.session_state.page == "quiz":
    st.title(f"{st.session_state.difficulty} Test")
    st.write(f"Student: **{st.session_state.student_name}**")
    st.write("---")
    
    with st.form("quiz_form"):
        user_answers = {}
        # Loop through the randomly selected questions instead of the whole bank
        for idx, q in enumerate(st.session_state.selected_quiz):
            st.markdown(f"**Q{idx+1}.** {q['question']}")
            
            if "image_svg" in q:
                st.markdown(q["image_svg"], unsafe_allow_html=True)
                st.write("") 
            
            st.markdown(
                f"**A)** {q['options'][0]}  \n"
                f"**B)** {q['options'][1]}  \n"
                f"**C)** {q['options'][2]}  \n"
                f"**D)** {q['options'][3]}"
            )
            
            letter_choice = st.radio("Select your answer:", ["A", "B", "C", "D"], key=q['id'], index=None, horizontal=True)
            letter_map = {"A": q['options'][0], "B": q['options'][1], "C": q['options'][2], "D": q['options'][3]}
            user_answers[q['id']] = letter_map.get(letter_choice)
            st.write("---")

        submitted = st.form_submit_button("Submit Answers")

        if submitted:
            st.session_state.user_answers = user_answers
            st.session_state.page = "results"
            st.rerun()

# ==========================================
# PAGE 3: EVALUATION, REPORTING & SOLUTIONS
# ==========================================
elif st.session_state.page == "results":
    st.header(f"Results for {st.session_state.student_name}")
    st.write(f"**Level Tested:** {st.session_state.difficulty}")
    
    score = 0
    total_questions = len(st.session_state.selected_quiz)
    category_scores = {}
    
    for q in st.session_state.selected_quiz:
        cat = q['category']
        if cat not in category_scores:
            category_scores[cat] = {"correct": 0, "total": 0}
        
        category_scores[cat]["total"] += 1
        
        if st.session_state.user_answers.get(q['id']) == q['answer']:
            score += 1
            category_scores[cat]["correct"] += 1

    percentage = (score / total_questions) * 100 if total_questions > 0 else 0

    st.subheader(f"Total Score: {score} / {total_questions} ({percentage:.0f}%)")
    
    if percentage >= 85:
        eval_text = "Excellent. You demonstrate strong mastery of this level."
    elif percentage >= 65:
        eval_text = "Solid foundation. You are on track with a few areas to review."
    else:
        eval_text = "Review recommended. We will focus on building core fundamentals."
        
    st.info(f"**Overall Evaluation:** {eval_text}")

    st.write("### Diagnostic Radar Analysis")
    radar_data = []
    for cat, data in category_scores.items():
        cat_percent = (data['correct'] / data['total']) * 100 if data['total'] > 0 else 0
        radar_data.append({"Category": cat, "Score": cat_percent})
        
    if len(radar_data) >= 3:
        df_radar = pd.DataFrame(radar_data)
        fig = px.line_polar(df_radar, r='Score', theta='Category', line_close=True, range_r=[0, 100], markers=True)
        fig.update_traces(fill='toself', line_color='#1f77b4')
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    st.write("### Detailed Breakdown")
    for cat, data in category_scores.items():
        cat_percent = (data['correct'] / data['total']) * 100 if data['total'] > 0 else 0
        st.progress(cat_percent / 100, text=f"{cat}: {data['correct']}/{data['total']} ({cat_percent:.0f}%)")

    st.write("---")
    with st.expander("📝 View Step-by-Step Solutions"):
        for idx, q in enumerate(st.session_state.selected_quiz):
            user_ans = st.session_state.user_answers.get(q['id'])
            correct_ans = q['answer']
            
            if user_ans == correct_ans:
                st.markdown(f"**Q{idx+1}. ✅ Correct**")
            else:
                st.markdown(f"**Q{idx+1}. ❌ Incorrect** (You chose: {user_ans})")
            
            st.markdown(f"**Question:** {q['question']}")
            if "image_svg" in q:
                st.markdown(q["image_svg"], unsafe_allow_html=True)
                
            st.markdown(f"**Correct Answer:** {correct_ans}")
            st.info(f"**Solution:** {q['solution']}")
            st.write("")

    try:
        sheet = init_gsheets()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [timestamp, st.session_state.student_name, st.session_state.difficulty, score, f"{percentage:.0f}%", eval_text]
        sheet.append_row(row)
        st.success("Your results have been securely saved to the teacher's database.")
    except Exception as e:
        st.error(f"Error saving to database: {e}")

    if st.button("Log Out / New Student"):
        st.session_state.page = "setup"
        st.session_state.student_name = ""
        st.session_state.difficulty = ""
        st.session_state.user_answers = {}
        st.session_state.selected_quiz = []
        st.rerun()
