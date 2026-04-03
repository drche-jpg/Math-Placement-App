import streamlit as st
import gspread
import datetime
import pandas as pd
import plotly.express as px
import random
from questions import all_questions

# --- 1. CORE FUNCTIONS ---
def init_gsheets():
    if "gcp_service_account" in st.secrets:
        creds_dict = dict(st.secrets["gcp_service_account"])
        client = gspread.service_account_from_dict(creds_dict)
    else:
        client = gspread.service_account(filename='credentials.json')
    return client.open("Math_Placement_Results").sheet1

# --- 2. INITIALIZATION ---
st.set_page_config(page_title="Math Placement Exam", layout="centered")

for key in ['page', 'student_name', 'difficulty', 'user_answers', 'selected_quiz']:
    if key not in st.session_state:
        st.session_state[key] = "setup" if key == 'page' else "" if key != 'selected_quiz' else []

# --- 3. PAGE LOGIC ---

# PAGE 1: SETUP
if st.session_state.page == "setup":
    st.title("Advanced Mathematics Placement Test")
    st.write("Please enter your information and select your difficulty level to begin.")
    
    with st.form("setup_form"):
        name = st.text_input("Full Student Name:")
        level = st.selectbox("Exam Difficulty:", ["Level 1: Easy", "Level 2: Intermediate", "Level 3: Difficult"])
        if st.form_submit_button("Begin Examination"):
            if name:
                level_qs = [q for q in all_questions if q['difficulty'] == level]
                # Randomly select 20 questions for this student
                st.session_state.selected_quiz = random.sample(level_qs, min(20, len(level_qs)))
                st.session_state.update({"student_name": name, "difficulty": level, "page": "quiz", "user_answers": {}})
                st.rerun()

# PAGE 2: QUIZ
elif st.session_state.page == "quiz":
    st.title(f"Assessment: {st.session_state.difficulty}")
    st.write(f"Candidate: **{st.session_state.student_name}**")
    
    with st.form("quiz_form"):
        temp_answers = {}
        for idx, q in enumerate(st.session_state.selected_quiz):
            st.markdown(f"### Question {idx+1}")
            st.markdown(f"{q['question']}")
            
            # 1. DISPLAY CHOICES HORIZONTALLY (Above bubbles)
            st.markdown(
                f"**A)** {q['options'][0]} &nbsp;&nbsp;&nbsp;&nbsp; "
                f"**B)** {q['options'][1]} &nbsp;&nbsp;&nbsp;&nbsp; "
                f"**C)** {q['options'][2]} &nbsp;&nbsp;&nbsp;&nbsp; "
                f"**D)** {q['options'][3]}"
            )
            
            # 2. SELECTION BUBBLES (Below choices)
            choice = st.radio("Select choice:", ["A", "B", "C", "D"], key=q['id'], index=None, horizontal=True)
            
            l_map = {"A": q['options'][0], "B": q['options'][1], "C": q['options'][2], "D": q['options'][3]}
            temp_answers[q['id']] = l_map.get(choice)
            st.write("---")
            
        if st.form_submit_button("Submit Final Answers"):
            st.session_state.user_answers = temp_answers
            st.session_state.page = "results"
            st.rerun()

# PAGE 3: RESULTS
elif st.session_state.page == "results":
    st.header(f"Performance Analysis: {st.session_state.student_name}")
    
    # Calculate Scores
    score = 0
    categories = ["Number Sense & Operations", "Pre-Algebra & Equations", "Geometry & Data", "Number Theory & Probability"]
    cat_stats = {c: {"c": 0, "t": 0} for c in categories}
    
    for q in st.session_state.selected_quiz:
        cat = q['category']
        cat_stats[cat]["t"] += 1
        if st.session_state.user_answers.get(q['id']) == q['answer']:
            score += 1
            cat_stats[cat]["c"] += 1
    
    perc = (score / 20) * 100
    st.subheader(f"Total Score: {score}/20 ({perc:.0f}%)")
    
    # Radar Chart
    df = pd.DataFrame([{"Category": k, "Score": (v['c']/v['t'])*100 if v['t']>0 else 0} for k,v in cat_stats.items()])
    fig = px.line_polar(df, r='Score', theta='Category', line_close=True, range_r=[0,100])
    fig.update_traces(fill='toself', line_color='#1f77b4')
    st.plotly_chart(fig, use_container_width=True)
    
    # Save to Google Sheet
    try:
        sheet = init_gsheets()
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cat_results = [f"{(cat_stats[c]['c']/cat_stats[c]['t'])*100:.0f}%" if cat_stats[c]['t']>0 else "0%" for c in categories]
        
        sheet.append_row([ts, st.session_state.student_name, st.session_state.difficulty, score, f"{perc:.0f}%", "Done"] + cat_results)
        st.success("Results successfully synchronized with teacher database.")
    except Exception as e:
        st.error(f"Database error: {e}")

    # Detailed Review
    with st.expander("Review Step-by-Step Solutions"):
        for idx, q in enumerate(st.session_state.selected_quiz):
            u_ans = st.session_state.user_answers.get(q['id'])
            correct = u_ans == q['answer']
            st.write(f"**Q{idx+1}. {'✅ Correct' if correct else '❌ Incorrect'}**")
            st.write(f"**Question:** {q['question']}")
            if not correct: st.write(f"**Your Answer:** {u_ans}")
            st.write(f"**Correct Answer:** {q['answer']}")
            st.info(f"**Solution:** {q['solution']}")
            st.write("")

    if st.button("Finish and Log Out"):
        st.session_state.page = "setup"
        st.rerun()
