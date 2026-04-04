import streamlit as st
import gspread
import datetime
import pandas as pd
import plotly.express as px
import random
from questions import all_questions

# --- 1. CORE FUNCTIONS ---
def init_gsheets():
    try:
        if "gcp_service_account" in st.secrets:
            creds_dict = dict(st.secrets["gcp_service_account"])
            client = gspread.service_account_from_dict(creds_dict)
            return client.open("Math_Placement_Results").sheet1
    except Exception:
        return None
    return None

# --- 2. CONFIG ---
st.set_page_config(page_title="Math Olympiad Placement", layout="wide")

for key in ['page', 'student_name', 'difficulty', 'user_answers', 'selected_quiz']:
    if key not in st.session_state:
        st.session_state[key] = "setup" if key == 'page' else "" if key != 'selected_quiz' else []

# --- 3. PAGE ROUTING ---

# PAGE 1: SETUP
if st.session_state.page == "setup":
    st.title("🏆 Mathematics Competition Placement")
    st.markdown("### Talent Search & Diagnostic Assessment")
    
    with st.form("setup_form"):
        name = st.text_input("Candidate Full Name:")
        level = st.selectbox("Select Difficulty:", ["Level 1: Easy", "Level 2: Intermediate", "Level 3: Difficult"])
        if st.form_submit_button("Initialize Examination"):
            if name:
                level_qs = [q for q in all_questions if q['difficulty'] == level]
                # 1. Random Sample of 20
                selected = random.sample(level_qs, min(20, len(level_qs)))
                
                # 2. DYNAMIC CHANGE: Shuffle the options for this specific session
                for item in selected:
                    random.shuffle(item['options'])
                    
                st.session_state.selected_quiz = selected
                st.session_state.update({"student_name": name, "difficulty": level, "page": "quiz", "user_answers": {}})
                st.rerun()

# PAGE 2: QUIZ
elif st.session_state.page == "quiz":
    st.title(f"Assessment Level: {st.session_state.difficulty}")
    st.info(f"Student: **{st.session_state.student_name}**")
    
    with st.form("quiz_form"):
        temp_answers = {}
        for idx, q in enumerate(st.session_state.selected_quiz):
            st.markdown(f"#### Problem {idx+1}")
            st.markdown(f"**{q['question']}**")
            
            if "image_svg" in q:
                st.markdown(q["image_svg"], unsafe_allow_html=True)
            
            # Display Options
            st.markdown(f"**A)** {q['options'][0]} &nbsp;&nbsp;&nbsp; **B)** {q['options'][1]} &nbsp;&nbsp;&nbsp; **C)** {q['options'][2]} &nbsp;&nbsp;&nbsp; **D)** {q['options'][3]}")
            
            # The bubbles (radio)
            choice = st.radio("Selection:", ["A", "B", "C", "D"], key=q['id'], index=None, horizontal=True)
            
            l_map = {"A": q['options'][0], "B": q['options'][1], "C": q['options'][2], "D": q['options'][3]}
            temp_answers[q['id']] = l_map.get(choice)
            st.divider()
            
        if st.form_submit_button("Submit Final Script"):
            st.session_state.user_answers = temp_answers
            st.session_state.page = "results"
            st.rerun()

# PAGE 3: RESULTS
elif st.session_state.page == "results":
    st.header(f"Performance Analysis: {st.session_state.student_name}")
    
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
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.metric("Total Score", f"{score}/20", f"{perc:.0f}%")
        df = pd.DataFrame([{"Category": k, "Score": (v['c']/v['t'])*100 if v['t']>0 else 0} for k,v in cat_stats.items()])
        fig = px.line_polar(df, r='Score', theta='Category', line_close=True, range_r=[0,100])
        fig.update_traces(fill='toself', line_color='#FF4B4B')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Pedagogical Evaluation")
        if perc >= 85:
            feedback = f"Excellent! {st.session_state.student_name} displays high fluency in complex problem-solving. We recommend immediate advancement to Olympiad training."
        elif perc >= 60:
            feedback = f"Commendable performance. Minor inconsistencies in multi-step execution were observed. Focused practice on logic and speed will bridge the gap to excellence."
        else:
            feedback = f"Diagnostic complete. Reinforcing foundational Grade 7-9 principles is recommended before attempting advanced competitive drills."
        st.write(feedback)
        st.info(f"**Growth Focus:** '{df.sort_values('Score').iloc[0]['Category']}'")

    # Save to Sheet
    sheet = init_gsheets()
    if sheet:
        try:
            ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cat_results = [f"{(cat_stats[c]['c']/cat_stats[c]['t'])*100:.0f}%" for c in categories]
            sheet.append_row([ts, st.session_state.student_name, st.session_state.difficulty, score, f"{perc:.0f}%", feedback] + cat_results)
        except Exception: pass

    with st.expander("Comprehensive Solution Key"):
        for idx, q in enumerate(st.session_state.selected_quiz):
            u_ans = st.session_state.user_answers.get(q['id'])
            correct = (u_ans == q['answer'])
            st.write(f"**Problem {idx+1}: {'✅' if correct else '❌'}**")
            st.write(f"Question: {q['question']}")
            st.success(f"Correct Answer: {q['answer']}")
            st.info(f"Logic: {q['solution']}")
            st.divider()

    if st.button("New Examination Session"):
        st.session_state.page = "setup"
        st.rerun()
