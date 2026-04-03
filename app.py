import streamlit as st
import gspread
import datetime
import pandas as pd
import plotly.express as px
import random
from questions import all_questions

# --- 1. CORE FUNCTIONS ---
def init_gsheets():
    """Initializes the connection to the Google Sheet database."""
    try:
        if "gcp_service_account" in st.secrets:
            creds_dict = dict(st.secrets["gcp_service_account"])
            client = gspread.service_account_from_dict(creds_dict)
            return client.open("Math_Placement_Results").sheet1
    except Exception:
        return None
    return None

# --- 2. INITIALIZATION ---
st.set_page_config(page_title="Math Olympiad Placement", layout="wide")

# Ensure all session state variables exist
for key in ['page', 'student_name', 'difficulty', 'user_answers', 'selected_quiz']:
    if key not in st.session_state:
        st.session_state[key] = "setup" if key == 'page' else "" if key != 'selected_quiz' else []

# --- 3. PAGE ROUTING ---

# --- PAGE 1: SETUP ---
if st.session_state.page == "setup":
    st.title("🏆 Mathematics Competition Placement")
    st.markdown("### Talent Search & Diagnostic Assessment")
    st.write("Please enter your information and select the assigned difficulty level to begin the examination.")
    
    with st.form("setup_form"):
        name = st.text_input("Full Student Name:")
        level = st.selectbox("Exam Difficulty:", ["Level 1: Easy", "Level 2: Intermediate", "Level 3: Difficult"])
        
        if st.form_submit_button("Initialize Examination"):
            if name:
                # Filter and randomly select 20 questions for this session
                level_qs = [q for q in all_questions if q['difficulty'] == level]
                if level_qs:
                    st.session_state.selected_quiz = random.sample(level_qs, min(20, len(level_qs)))
                    st.session_state.update({
                        "student_name": name, 
                        "difficulty": level, 
                        "page": "quiz", 
                        "user_answers": {}
                    })
                    st.rerun()
                else:
                    st.error("Error: No questions found for this level in questions.py.")
            else:
                st.error("Please enter a student name to proceed.")

# --- PAGE 2: QUIZ ---
elif st.session_state.page == "quiz":
    st.title(f"Assessment: {st.session_state.difficulty}")
    st.info(f"Candidate: **{st.session_state.student_name}** | Questions: 20")
    
    with st.form("quiz_form"):
        temp_answers = {}
        for idx, q in enumerate(st.session_state.selected_quiz):
            st.markdown(f"### Problem {idx+1}")
            st.markdown(f"**{q['question']}**")
            
            # Render SVG diagram if available
            if "image_svg" in q:
                st.markdown(q["image_svg"], unsafe_allow_html=True)
            
            # Choice text ABOVE bubbles (No vertical bars)
            st.markdown(
                f"**A)** {q['options'][0]} &nbsp;&nbsp;&nbsp;&nbsp; "
                f"**B)** {q['options'][1]} &nbsp;&nbsp;&nbsp;&nbsp; "
                f"**C)** {q['options'][2]} &nbsp;&nbsp;&nbsp;&nbsp; "
                f"**D)** {q['options'][3]}"
            )
            
            # Selection bubbles BELOW choices
            choice = st.radio("Select choice:", ["A", "B", "C", "D"], key=q['id'], index=None, horizontal=True)
            
            # Map choice back to full option text for scoring
            l_map = {"A": q['options'][0], "B": q['options'][1], "C": q['options'][2], "D": q['options'][3]}
            temp_answers[q['id']] = l_map.get(choice)
            st.divider()
            
        if st.form_submit_button("Submit Final Script"):
            st.session_state.user_answers = temp_answers
            st.session_state.page = "results"
            st.rerun()

# --- PAGE 3: RESULTS ---
elif st.session_state.page == "results":
    st.header(f"Performance Analysis: {st.session_state.student_name}")
    
    # Calculate Scores and Categories
    score = 0
    categories = ["Number Sense & Operations", "Pre-Algebra & Equations", "Geometry & Data", "Number Theory & Probability"]
    cat_stats = {c: {"c": 0, "t": 0} for c in categories}
    
    for q in st.session_state.selected_quiz:
        cat = q['category']
        cat_stats[cat]["t"] += 1
        if st.session_state.user_answers.get(q['id']) == q['answer']:
            score += 1
            cat_stats[cat]["c"] += 1
    
    perc = (score / len(st.session_state.selected_quiz)) * 100
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.metric("Final Score", f"{score}/20", f"{perc:.0f}%")
        # Radar Chart Generation
        radar_df = pd.DataFrame([{"Category": k, "Score": (v['c']/v['t'])*100 if v['t']>0 else 0} for k,v in cat_stats.items()])
        fig = px.line_polar(radar_df, r='Score', theta='Category', line_close=True, range_r=[0,100])
        fig.update_traces(fill='toself', line_color='#FF4B4B')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Pedagogical Evaluation")
        # 100-word Feedback Logic
        if perc >= 85:
            feedback = (
                f"Exceptional performance by {st.session_state.student_name}. You have demonstrated a high level of "
                "mathematical fluency and an impressive ability to navigate complex, multi-step problems with precision. "
                "Your results indicate a mastery of the core curriculum at the Grade 7-9 level. This level of conceptual "
                "understanding and logical reasoning is rare and suggests you are well-prepared for competitive math "
                "environments. You exhibit strong critical thinking skills that allow you to apply abstract theories "
                "to practical calculations effortlessly."
            )
            recommendation = "Focus on advanced Olympiad-style problem solving to further sharpen your skills."
        elif perc >= 60:
            feedback = (
                f"{st.session_state.student_name} has shown a solid and consistent understanding of the fundamental concepts "
                "within this assessment. You successfully identified the correct strategies for most problems, though some "
                "minor errors in calculation or conceptual application in more challenging questions were observed. "
                "Overall, you possess a healthy mathematical foundation that will serve as a strong base for future growth. "
                "With continued practice and a focus on detail, your path to full mastery is very clear."
            )
            recommendation = "Practice timed drills to increase both speed and accuracy in your calculations."
        else:
            feedback = (
                f"This assessment serves as a valuable diagnostic for {st.session_state.student_name}. While there are "
                "clear signs of mathematical potential, the results suggest that several foundational concepts require "
                "further reinforcement. Strengthening your core skills in your lower-scoring categories will provide the "
                "confidence needed to tackle the more complex problems you encountered. Mathematics is a cumulative "
                "subject, and taking the time now to bridge these gaps will lead to much greater success later."
            )
            recommendation = "Focus on targeted review sessions for your lowest-scoring categories."

        st.write(feedback)
        st.info(f"**Recommendation:** {recommendation}")
        st.caption(f"**Focus Area:** Strengthen '{radar_df.sort_values('Score').iloc[0]['Category']}' for optimal growth.")

    # Save to Google Sheet
    sheet = init_gsheets()
    if sheet:
        try:
            ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cat_row = [f"{(cat_stats[c]['c']/cat_stats[c]['t'])*100:.0f}%" if cat_stats[c]['t']>0 else "0%" for c in categories]
            # Save: TS, Name, Level, Score, %, Full Feedback, and 4 Cat Scores
            sheet.append_row([ts, st.session_state.student_name, st.session_state.difficulty, score, f"{perc:.0f}%", feedback] + cat_row)
            st.success("Results successfully synchronized with teacher database.")
        except Exception:
            st.warning("Score recorded locally, but cloud database sync failed.")

    # Detailed Review Section
    with st.expander("Review Comprehensive Solution Guide"):
        for idx, q in enumerate(st.session_state.selected_quiz):
            u_ans = st.session_state.user_answers.get(q['id'])
            correct = (u_ans == q['answer'])
            st.write(f"**Problem {idx+1}: {'✅ Correct' if correct else '❌ Incorrect'}**")
            st.write(f"**Question:** {q['question']}")
            if "image_svg" in q:
                st.markdown(q["image_svg"], unsafe_allow_html=True)
            if not correct:
                st.write(f"**Your Selection:** {u_ans}")
            st.write(f"**Correct Answer:** {q['answer']}")
            st.info(f"**Solution Logic:** {q['solution']}")
            st.write("")

    if st.button("Finish and Return to Home"):
        st.session_state.page = "setup"
        st.rerun()
