import streamlit as st
import gspread
import datetime
import pandas as pd
import plotly.express as px
import random
import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from google.oauth2 import service_account
from questions import all_questions

# --- 1. CONFIG & AUTH ---
st.set_page_config(page_title="Math Placement Test", layout="centered")

def init_gsheets():
    if "gcp_service_account" in st.secrets:
        creds_dict = dict(st.secrets["gcp_service_account"])
        client = gspread.service_account_from_dict(creds_dict)
    else:
        client = gspread.service_account(filename='credentials.json')
    return client.open("Math_Placement_Results").sheet1

def upload_to_drive(file_name, image_bytes):
    if "gcp_service_account" in st.secrets:
        creds_dict = dict(st.secrets["gcp_service_account"])
        credentials = service_account.Credentials.from_service_account_info(creds_dict)
        service = build('drive', 'v3', credentials=credentials)
        file_metadata = {'name': file_name, 'mimeType': 'image/png'}
        media = MediaIoBaseUpload(io.BytesIO(image_bytes), mimetype='image/png')
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id')
    return None

# --- 2. SESSION STATE ---
for key in ['page', 'student_name', 'difficulty', 'user_answers', 'selected_quiz']:
    if key not in st.session_state:
        st.session_state[key] = "setup" if key == 'page' else "" if key != 'selected_quiz' else []
if 'user_answers' not in st.session_state: st.session_state.user_answers = {}

# --- 3. PAGE ROUTING ---
# PAGE 1: SETUP
if st.session_state.page == "setup":
    st.title("Math Placement Test")
    with st.form("setup_form"):
        name = st.text_input("Student Name:")
        level = st.selectbox("Difficulty:", ["Level 1: Easy", "Level 2: Intermediate", "Level 3: Difficult"])
        if st.form_submit_button("Start Test"):
            if name:
                st.session_state.update({"student_name": name, "difficulty": level, "page": "quiz"})
                level_qs = [q for q in all_questions if q['difficulty'] == level]
                st.session_state.selected_quiz = random.sample(level_qs, min(20, len(level_qs)))
                st.rerun()

# PAGE 2: QUIZ
elif st.session_state.page == "quiz":
    st.title(st.session_state.difficulty)
    st.write(f"Student: **{st.session_state.student_name}**")
    
    with st.form("quiz_form"):
        temp_answers = {}
        for idx, q in enumerate(st.session_state.selected_quiz):
            st.markdown(f"**Q{idx+1}.** {q['question']}")
            
            if "image_svg" in q:
                st.markdown(q["image_svg"], unsafe_allow_html=True)
            
            # 1. Choices moved ABOVE the radio buttons (no vertical bars)
            st.markdown(
                f"**A)** {q['options'][0]} &nbsp;&nbsp; "
                f"**B)** {q['options'][1]} &nbsp;&nbsp; "
                f"**C)** {q['options'][2]} &nbsp;&nbsp; "
                f"**D)** {q['options'][3]}"
            )
            
            # 2. Radio buttons moved BELOW the choices
            choice = st.radio("Select your answer:", ["A", "B", "C", "D"], key=q['id'], index=None, horizontal=True)
            
            # Logic to map the letter to the actual option text for scoring
            letter_map = {"A": q['options'][0], "B": q['options'][1], "C": q['options'][2], "D": q['options'][3]}
            temp_answers[q['id']] = letter_map.get(choice) if choice else None
            
            st.write("---")
            
        if st.form_submit_button("Submit"):
            st.session_state.user_answers = temp_answers
            st.session_state.page = "results"
            st.rerun()

# PAGE 3: RESULTS
elif st.session_state.page == "results":
    st.header(f"Results: {st.session_state.student_name}")
    score = 0
    cat_stats = {}
    for q in st.session_state.selected_quiz:
        cat = q['category']
        if cat not in cat_stats: cat_stats[cat] = {"c": 0, "t": 0}
        cat_stats[cat]["t"] += 1
        if st.session_state.user_answers.get(q['id']) == q['answer']:
            score += 1
            cat_stats[cat]["c"] += 1
    
    perc = (score / len(st.session_state.selected_quiz)) * 100
    st.subheader(f"Score: {score}/20 ({perc:.0f}%)")
    
    # Radar Chart
    df = pd.DataFrame([{"Category": k, "Score": (v['c']/v['t'])*100} for k,v in cat_stats.items()])
    fig = px.line_polar(df, r='Score', theta='Category', line_close=True, range_r=[0,100])
    fig.update_traces(fill='toself')
    st.plotly_chart(fig)
    
    # Save Image & Data
    try:
        fname = f"{st.session_state.student_name}_{st.session_state.difficulty}".replace(" ","_")
        upload_to_drive(f"{fname}.png", fig.to_image(format="png"))
        
        sheet = init_gsheets()
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        c_scores = [f"{(cat_stats.get(c,{'c':0,'t':1})['c']/cat_stats.get(c,{'c':0,'t':1})['t'])*100:.0f}%" for c in ["Number Sense & Operations", "Pre-Algebra & Equations", "Geometry & Data", "Number Theory & Probability"]]
        sheet.append_row([ts, st.session_state.student_name, st.session_state.difficulty, score, f"{perc:.0f}%", "Done"] + c_scores)
        st.success("Results and Radar chart saved!")
    except Exception as e: st.error(f"Save error: {e}")

    if st.button("New Test"):
        st.session_state.page = "setup"
        st.rerun()
