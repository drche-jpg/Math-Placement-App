import streamlit as st
import gspread
import datetime
import pandas as pd
import plotly.express as px

# --- 1. GOOGLE SHEETS SETUP ---
def init_gsheets():
    if "gcp_service_account" in st.secrets:
        creds_dict = dict(st.secrets["gcp_service_account"])
        client = gspread.service_account_from_dict(creds_dict)
    else:
        client = gspread.service_account(filename='credentials.json')
        
    sheet = client.open("Math_Placement_Results").sheet1
    return sheet

# --- 2. QUIZ DATA & SYLLABUS MAPPING ---
quiz_data = [
    # Number Sense & Operations
    {
        "id": 1,
        "category": "Number Sense & Operations",
        "question": r"Evaluate: $\left( -\frac{2}{3} \right)^2 \div \frac{4}{9} - (-3)^3$",
        "options": ["28", "-26", "26", "-28"],
        "answer": "28"
    },
    {
        "id": 2,
        "category": "Number Sense & Operations",
        "question": "A store marks up a $40 item by 25%. During a sale, they apply a 10% discount to the new price. What is the final sale price?",
        "options": ["$45", "$42.50", "$46", "$50"],
        "answer": "$45"
    },
    {
        "id": 3,
        "category": "Number Sense & Operations",
        "question": r"Calculate the product and express in scientific notation: $ (3.2 \times 10^4) \times (5 \times 10^3) $",
        "options": [r"$1.6 \times 10^8$", r"$16 \times 10^7$", r"$1.6 \times 10^7$", r"$8.2 \times 10^7$"],
        "answer": r"$1.6 \times 10^8$"
    },
    {
        "id": 4,
        "category": "Number Sense & Operations",
        "question": r"Simplify the complex fraction: $ \frac{\frac{1}{2} + \frac{1}{3}}{\frac{1}{4}} $",
        "options": ["10/3", "5/12", "12/5", "3/10"],
        "answer": "10/3"
    },
    {
        "id": 5,
        "category": "Number Sense & Operations",
        "question": "Two flashing warning lights turn on at the exact same time. Light A flashes every 18 seconds, and Light B flashes every 24 seconds. How many seconds will pass before they flash together again?",
        "options": ["72 seconds", "36 seconds", "144 seconds", "48 seconds"],
        "answer": "72 seconds"
    },
    
    # Pre-Algebra & Equations
    {
        "id": 6,
        "category": "Pre-Algebra & Equations",
        "question": r"Solve for x: $ \frac{1}{2}(4x - 6) = 3x - 11 $",
        "options": ["x = 8", "x = 4", "x = -8", "x = 14"],
        "answer": "x = 8"
    },
    {
        "id": 7,
        "category": "Pre-Algebra & Equations",
        "question": r"Solve the inequality for x: $ -3(x - 4) \leq 15 $",
        "options": [r"$x \geq -1$", r"$x \leq -1$", r"$x \geq 9$", r"$x \leq 9$"],
        "answer": r"$x \geq -1$"
    },
    {
        "id": 8,
        "category": "Pre-Algebra & Equations",
        "question": r"Find the value of x and y that satisfies both equations: $ 2x + y = 10 $ and $ x - y = 2 $",
        "options": ["x = 4, y = 2", "x = 2, y = 4", "x = 6, y = -2", "x = 3, y = 1"],
        "answer": "x = 4, y = 2"
    },
    {
        "id": 9,
        "category": "Pre-Algebra & Equations",
        "question": "The sum of three consecutive even integers is 84. What is the largest of these three integers?",
        "options": ["30", "28", "32", "26"],
        "answer": "30"
    },
    {
        "id": 10,
        "category": "Pre-Algebra & Equations",
        "question": r"If $ f(x) = -2x^2 + 5x - 3 $, find the value of $ f(-2) $.",
        "options": ["-21", "-5", "-13", "9"],
        "answer": "-21"
    },

    # Geometry & Data
    {
        "id": 11,
        "category": "Geometry & Data",
        "question": "A rectangular garden is 12 meters long and 5 meters wide. What is the exact length of a straight diagonal path connecting two opposite corners?",
        "options": ["13 meters", "17 meters", "10.9 meters", "14 meters"],
        "answer": "13 meters"
    },
    {
        "id": 12,
        "category": "Geometry & Data",
        "question": "A solid cylinder has a radius of 3 cm and a height of 10 cm. What is its exact volume?",
        "options": [r"$90\pi \text{ cm}^3$", r"$30\pi \text{ cm}^3$", r"$60\pi \text{ cm}^3$", r"$180\pi \text{ cm}^3$"],
        "answer": r"$90\pi \text{ cm}^3$"
    },
    {
        "id": 13,
        "category": "Geometry & Data",
        "question": r"Two parallel lines are intersected by a transversal line. If one interior angle measures $ (3x - 15)^\circ $ and its alternate interior angle measures $ (2x + 10)^\circ $, find the value of x.",
        "options": ["x = 25", "x = 5", "x = 35", "x = 15"],
        "answer": "x = 25"
    },
    {
        "id": 14,
        "category": "Geometry & Data",
        "question": "A student has test scores of 82, 86, and 90. What score must they get on their fourth test to achieve a mean score of exactly 88?",
        "options": ["94", "92", "96", "88"],
        "answer": "94"
    },
    
    # Number Theory & Probability
    {
        "id": 15,
        "category": "Number Theory & Probability",
        "question": "A bag contains 4 red marbles and 6 blue marbles. If two marbles are drawn at random without replacement, what is the probability that both drawn marbles are red?",
        "options": ["2/15", "4/25", "1/5", "8/45"],
        "answer": "2/15"
    },
    {
        "id": 16,
        "category": "Number Theory & Probability",
        "question": "How many positive integer divisors does 120 have?",
        "options": ["16", "12", "14", "18"],
        "answer": "16"
    },
    {
        "id": 17,
        "category": "Number Theory & Probability",
        "question": r"What is the units digit of $ 7^{45} $?",
        "options": ["7", "9", "3", "1"],
        "answer": "7"
    },
    {
        "id": 18,
        "category": "Number Theory & Probability",
        "question": "A teacher has 84 red pens, 126 blue pens, and 210 black pens. They want to pack them into identical boxes such that each box has the same combination of pens with none left over. What is the greatest number of boxes they can pack?",
        "options": ["42", "21", "14", "6"],
        "answer": "42"
    },
    {
        "id": 19,
        "category": "Number Theory & Probability",
        "question": "Using the letters A, B, C, D, and E, how many different 3-letter arrangements can be formed if no letter is repeated?",
        "options": ["60", "10", "15", "120"],
        "answer": "60"
    },
    {
        "id": 20,
        "category": "Number Theory & Probability",
        "question": "Two fair six-sided dice are rolled simultaneously. What is the probability that the sum of the numbers rolled is a prime number?",
        "options": ["5/12", "7/18", "1/3", "1/4"],
        "answer": "5/12"
    }
]

# --- 3. UI AND LOGIC ---
st.set_page_config(page_title="Grade 7 Math Placement", layout="centered")

st.title("Grade 7 Advanced Math Placement Test")
st.write("Please answer all questions. Your performance report will be generated immediately upon submission.")

if 'submitted' not in st.session_state:
    st.session_state.submitted = False

if not st.session_state.submitted:
    with st.form("quiz_form"):
        student_name = st.text_input("Student Name:")
        st.write("---")
        
        user_answers = {}
        for idx, q in enumerate(quiz_data):
            st.markdown(f"**Q{idx+1}.** {q['question']}")
            
            # Display options using markdown so math renders perfectly
            st.markdown(
                f"**A)** {q['options'][0]}  \n"
                f"**B)** {q['options'][1]}  \n"
                f"**C)** {q['options'][2]}  \n"
                f"**D)** {q['options'][3]}"
            )
            
            # Simple A/B/C/D radio buttons
            letter_choice = st.radio("Select your answer:", ["A", "B", "C", "D"], key=q['id'], index=None, horizontal=True)
            
            # Map letter back to answer text
            letter_map = {"A": q['options'][0], "B": q['options'][1], "C": q['options'][2], "D": q['options'][3]}
            user_answers[q['id']] = letter_map.get(letter_choice)
            
            st.write("---")

        submitted = st.form_submit_button("Submit Answers")

        if submitted:
            if not student_name:
                st.error("Please enter your name before submitting.")
            else:
                st.session_state.student_name = student_name
                st.session_state.user_answers = user_answers
                st.session_state.submitted = True
                st.rerun()

# --- 4. EVALUATION, REPORTING & RADAR CHART ---
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

    for q in quiz_data:
        cat = q['category']
        category_scores[cat]["total"] += 1
        
        if st.session_state.user_answers[q['id']] == q['answer']:
            score += 1
            category_scores[cat]["correct"] += 1

    percentage = (score / total_questions) * 100

    st.subheader(f"Total Score: {score} / {total_questions} ({percentage:.0f}%)")
    
    if percentage >= 85:
        eval_text = "Excellent. You demonstrate strong mastery of advanced topics and are highly prepared for the curriculum."
    elif percentage >= 65:
        eval_text = "Solid foundation. You are ready for the class, with some specific areas to review."
    else:
        eval_text = "Review recommended. We will focus on building core fundamentals before moving to complex topics."
        
    st.info(f"**Overall Evaluation:** {eval_text}")

    # --- Generate Radar Chart ---
    st.write("### Diagnostic Radar Analysis")
    
    radar_data = []
    for cat, data in category_scores.items():
        if data['total'] > 0:
            cat_percent = (data['correct'] / data['total']) * 100
        else:
            cat_percent = 0
        radar_data.append({"Category": cat, "Score": cat_percent})
        
    df_radar = pd.DataFrame(radar_data)

    fig = px.line_polar(
        df_radar, 
        r='Score', 
        theta='Category', 
        line_close=True,
        range_r=[0, 100],
        markers=True
    )
    fig.update_traces(fill='toself', line_color='#1f77b4')
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100])
        ),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

    # --- Diagnostic Breakdown Progress Bars ---
    st.write("### Detailed Breakdown")
    for cat, data in category_scores.items():
        if data['total'] > 0:
            cat_percent = (data['correct'] / data['total']) * 100
            st.progress(cat_percent / 100, text=f"{cat}: {data['correct']}/{data['total']} ({cat_percent:.0f}%)")

    # Save to Google Sheets
    try:
        sheet = init_gsheets()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        row = [timestamp, st.session_state.student_name, score, f"{percentage:.0f}%", eval_text]
        sheet.append_row(row)
        st.success("Your results have been securely saved to the teacher's database.")
    except Exception as e:
        st.error(f"Error saving to database: {e}")

    if st.button("Reset / Take Again"):
        st.session_state.submitted = False
        st.rerun()
