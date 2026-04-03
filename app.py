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

# --- 3. PAGE ROUTING ---

# PAGE 1: SETUP
if st.session_state.page == "setup":
    st.title("Math Placement Test")
    with st.form("setup_form"):
        name = st.text_input("Student Name:")
        level = st.selectbox("Difficulty:", ["Level 1: Easy", "Level 2: Intermediate", "Level 3: Difficult"])
        if st.form_submit_button("Start Test"):
            if name:
                level_qs = [q for q in all_questions if q['difficulty'] == level]
                st.session_state.update({
                    "student_name": name, 
                    "difficulty": level, 
                    "page": "quiz",
                    "selected_quiz": random.sample(level_qs, min(20, len(level_qs))),
                    "user_answers": {}
                })
                st.rerun()

# PAGE 2: QUIZ
elif st.session_state.page == "quiz":
    st.title(st.session_state.difficulty)
    st.write(f"Student: **{st.session_state.student_name}**")
    
    with st.form("quiz_form"):
        temp_answers = {}
        for idx, q in enumerate(st.session_state.selected_quiz):
            st.markdown(f"**Q{idx+1}.** {q['question']}")
            
            # Choice text moved ABOVE radio
            st.markdown(
                f"**A)** {q['options'][0]} &nbsp;&nbsp;&nbsp; "
                f"**B)** {q['options'][1]} &nbsp;&nbsp;&nbsp; "
                f"**C)** {q['options'][2]} &nbsp;&nbsp;&nbsp; "
                f"**D)** {q['options'][3]}"
            )
            
            # Radio buttons BELOW choice text
            choice = st.radio("Select answer:", ["A", "B", "C", "D"], key=q['id'], index=None, horizontal=True)
            
            l_map = {"A": q['options'][0], "B": q['options'][1], "C": q['options'][2], "D": q['options'][3]}
            temp_answers[q['id']] = l_map.get(choice)
            st.write("---")
            
        if st.form_submit_button("Submit"):
            st.session_state.user_answers = temp_answers
            st.session_state.page = "results"
            st.rerun()

# PAGE 3: RESULTS
elif st.session_state.page == "results":
    st.header(f"Results: {st.session_state.student_name}")
    
    score = 0
    cat_stats = {
        "Number Sense & Operations": {"c": 0, "t": 0},
        "Pre-Algebra & Equations": {"c": 0, "t": 0},
        "Geometry & Data": {"c": 0, "t": 0},
        "Number Theory & Probability": {"c": 0, "t": 0}
    }
    
    for q in st.session_state.selected_quiz:
        cat = q['category']
        cat_stats[cat]["t"] += 1
        if st.session_state.user_answers.get(q['id']) == q['answer']:
            score += 1
            cat_stats[cat]["c"] += 1
    
    perc = (score / len(st.session_state.selected_quiz)) * 100
    st.subheader(f"Total Score: {score}/20 ({perc:.0f}%)")
    
    # Radar Chart
    df = pd.DataFrame([{"Category": k, "Score": (v['c']/v['t'])*100 if v['t']>0 else 0} for k,v in cat_stats.items()])
    fig = px.line_polar(df, r='Score', theta='Category', line_close=True, range_r=[0,100])
    fig.update_traces(fill='toself')
    st.plotly_chart(fig)
    
    # Save Image & Data
    try:
        # 1. Save Image to Drive
        fname = f"{st.session_state.student_name}_{st.session_state.difficulty}".replace(" ","_")
        img_bytes = fig.to_image(format="png")
        upload_to_drive(f"{fname}.png", img_bytes)
        
        # 2. Save Data to Sheets
        sheet = init_gsheets()
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Build category score list for the row
        cat_row = []
        for c in ["Number Sense & Operations", "Pre-Algebra & Equations", "Geometry & Data", "Number Theory & Probability"]:
            s = cat_stats.get(c, {'c':0,'t':1})
            cat_row.append(f"{(s['c']/s['t'])*100:.0f}%")
            
        sheet.append_row([ts, st.session_state.student_name, st.session_state.difficulty, score, f"{perc:.0f}%", "Completed"] + cat_row)
        st.success("Analysis complete. Radar chart and scores have been recorded.")
        
    except Exception as e:
        st.warning(f"Recorded results, but encountered a save error: {e}")

    # Solutions
    with st.expander("View Step-by-Step Solutions"):
        for idx, q in enumerate(st.session_state.selected_quiz):
            u_ans = st.session_state.user_answers.get(q['id'])
            status = "✅" if u_ans == q['answer'] else f"❌ (You chose: {u_ans})"
            st.write(f"**Q{idx+1}. {status}**")
            st.write(f"Question: {q['question']}")
            st.info(f"Solution: {q['solution']}")

    if st.button("New Test"):
        st.session_state.page = "setup"
        st.rerun()
