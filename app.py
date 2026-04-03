import streamlit as st
import gspread
import datetime
import pandas as pd
import json

# --- 1. GOOGLE SHEETS SETUP ---
def init_gsheets():
    # This checks if we are running on Streamlit Cloud (which uses st.secrets)
    if "gcp_service_account" in st.secrets:
        creds_dict = dict(st.secrets["gcp_service_account"])
        client = gspread.service_account_from_dict(creds_dict)
    # If not on Streamlit Cloud, it assumes we are running locally and looks for the file
    else:
        client = gspread.service_account(filename='credentials.json')
        
    sheet = client.open("Math_Placement_Results").sheet1
    return sheet

# --- 2. QUIZ DATA & SYLLABUS MAPPING ---
# Map questions to specific skills for the performance report
quiz_data = [
    {
        "id": 1,
        "category": "Number Sense & Operations",
        "question": "Evaluate: $ \\left( -\\frac{2}{3} \\right)^2 \\div \\frac{4}{9} - (-3)^3 $",
        "options": ["28", "-26", "26", "-28"],
        "answer": "28"
    },
    {
        "id": 2,
        "category": "Pre-Algebra & Equations",
        "question": "Solve for x: $ \\frac{1}{2}(4x - 6) = 3x - 11 $",
        "options": ["x = 8", "x = 4", "x = -8", "x = 14"],
        "answer": "x = 8"
    },
    {
        "id": 3,
        "category": "Geometry & Data",
        "question": "A solid cylinder has a radius of 3 cm and a height of 10 cm. What is its exact volume?",
        "options": ["$90\\pi$ cm$^3$", "$30\\pi$ cm$^3$", "$60\\pi$ cm$^3$", "$180\\pi$ cm$^3$"],
        "answer": "$90\\pi$ cm$^3$"
    },
    {
        "id": 4,
        "category": "Number Theory & Probability",
        "question": "How many positive integer divisors does 120 have?",
        "options": ["16", "12", "14", "18"],
        "answer": "16"
    }
    # Add the remaining 16 questions here following the same format
]

# --- 3. UI AND LOGIC ---
st.set_page_config(page_title="Grade 7-8 Math Placement", layout="centered")

st.title("Grade 7-8 Advanced Math Placement Test")
st.write("Please answer all questions. Your performance report will be generated immediately upon submission.")

# Initialize session state to track if quiz is submitted
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

if not st.session_state.submitted:
    with st.form("quiz_form"):
        student_name = st.text_input("Student Name:")
        
        st.write("---")
        user_answers = {}
        for idx, q in enumerate(quiz_data):
            st.markdown(f"**Q{idx+1}.** {q['question']}")
            # Radio buttons for options
            user_answers[q['id']] = st.radio("Select answer:", q['options'], key=q['id'], index=None)
            st.write("") 

        submitted = st.form_submit_button("Submit Answers")

        if submitted:
            if not student_name:
                st.error("Please enter your name before submitting.")
            else:
                st.session_state.student_name = student_name
                st.session_state.user_answers = user_answers
                st.session_state.submitted = True
                st.rerun()

# --- 4. EVALUATION & REPORTING ---
if st.session_state.submitted:
    st.header(f"Results for {st.session_state.student_name}")
    
    score = 0
    total_questions = len(quiz_data)
    category_scores = {
        "Number Sense & Operations": {"correct": 0, "total": 0},
        "Pre-Algebra & Equations": {"correct": 0, "total": 0},
        "Geometry & Data": {"correct": 0, "total": 0},
        "Number Theory & Probability": {"correct": 0, "total": 0}
    }

    # Calculate scores
    for q in quiz_data:
        cat = q['category']
        category_scores[cat]["total"] += 1
        
        if st.session_state.user_answers[q['id']] == q['answer']:
            score += 1
            category_scores[cat]["correct"] += 1

    percentage = (score / total_questions) * 100

    # Generate Performance Report
    st.subheader(f"Total Score: {score} / {total_questions} ({percentage:.1f}%)")
    
    if percentage >= 85:
        eval_text = "Excellent. You demonstrate strong mastery of advanced topics and are highly prepared for the curriculum."
    elif percentage >= 65:
        eval_text = "Solid foundation. You are ready for the class, with some specific areas to review."
    else:
        eval_text = "Review recommended. We will focus on building core fundamentals before moving to complex topics."
        
    st.info(f"**Overall Evaluation:** {eval_text}")

    st.write("### Diagnostic Breakdown")
    for cat, data in category_scores.items():
        if data['total'] > 0:
            cat_percent = (data['correct'] / data['total']) * 100
            st.progress(cat_percent / 100, text=f"{cat}: {data['correct']}/{data['total']} ({cat_percent:.0f}%)")

    # Save to Google Sheets
    try:
        sheet = init_gsheets()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [timestamp, st.session_state.student_name, score, f"{percentage:.1f}%", eval_text]
        sheet.append_row(row)
        st.success("Your results have been securely saved to the teacher's database.")
    except Exception as e:
        st.error(f"Error saving to database: {e}")

    if st.button("Reset / Take Again"):
        st.session_state.submitted = False
        st.rerun()