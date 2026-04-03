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

# --- 2. QUIZ DATA (Divided into Levels) ---
quiz_data = [
    # ==========================================
    # LEVEL 1: EASY (Foundations)
    # ==========================================
    {
        "id": 101, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations",
        "question": r"Evaluate: $15 - (-4) + 3 \times 2$",
        "options": ["25", "13", "11", "26"], "answer": "25",
        "solution": r"Use Order of Operations (PEMDAS). First multiply: $3 \times 2 = 6$. The equation is $15 - (-4) + 6$. Subtracting a negative is adding: $15 + 4 + 6 = 25$."
    },
    {
        "id": 102, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations",
        "question": r"Convert the fraction $\frac{3}{5}$ to a percentage.",
        "options": ["30%", "60%", "35%", "50%"], "answer": "60%",
        "solution": r"To convert a fraction to a percent, multiply the numerator and denominator by a number that makes the denominator 100. Multiply by 20: $\frac{3 \times 20}{5 \times 20} = \frac{60}{100} = 60\%$."
    },
    {
        "id": 103, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations",
        "question": r"Solve for x: $4x + 7 = 23$",
        "options": ["x = 3", "x = 4", "x = 5", "x = 6"], "answer": "x = 4",
        "solution": r"Subtract 7 from both sides: $4x = 16$. Divide by 4: $x = 4$."
    },
    {
        "id": 104, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations",
        "question": r"If $y = 3x - 2$, what is the value of y when $x = 5$?",
        "options": ["13", "15", "17", "11"], "answer": "13",
        "solution": r"Substitute 5 for x: $y = 3(5) - 2$. Multiply first: $y = 15 - 2$. Subtract: $y = 13$."
    },
    {
        "id": 105, "difficulty": "Level 1: Easy", "category": "Geometry & Data",
        "question": r"Find the area of a triangle with a base of 10 cm and a height of 6 cm.",
        "options": ["60 cm²", "30 cm²", "16 cm²", "120 cm²"], "answer": "30 cm²",
        "solution": r"The formula for the area of a triangle is $A = \frac{1}{2}bh$. Substitute the values: $A = \frac{1}{2}(10)(6) = 5 \times 6 = 30$."
    },
    {
        "id": 106, "difficulty": "Level 1: Easy", "category": "Geometry & Data",
        "question": r"What is the perimeter of a rectangle with length 8m and width 3m?",
        "options": ["24m", "11m", "22m", "16m"], "answer": "22m",
        "solution": r"Perimeter is the sum of all sides: $P = 2l + 2w$. $P = 2(8) + 2(3) = 16 + 6 = 22$."
    },
    {
        "id": 107, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability",
        "question": r"What is the Greatest Common Factor (GCF) of 12 and 18?",
        "options": ["2", "3", "6", "36"], "answer": "6",
        "solution": r"Factors of 12: 1, 2, 3, 4, 6, 12. Factors of 18: 1, 2, 3, 6, 9, 18. The largest factor they share is 6."
    },
    {
        "id": 108, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability",
        "question": r"If you roll a standard 6-sided die, what is the probability of rolling an even number?",
        "options": ["1/6", "1/3", "1/2", "2/3"], "answer": "1/2",
        "solution": r"The even numbers on a die are 2, 4, and 6. That is 3 successful outcomes out of 6 total possibilities. $\frac{3}{6}$ simplifies to $\frac{1}{2}$."
    },
    {
        "id": 109, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations",
        "question": r"Evaluate: $4^3$",
        "options": ["12", "16", "64", "256"], "answer": "64",
        "solution": r"$4^3$ means 4 multiplied by itself three times. $4 \times 4 \times 4 = 16 \times 4 = 64$."
    },
    {
        "id": 110, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations",
        "question": r"Simplify: $3(a + 4) - 2a$",
        "options": ["a + 12", "5a + 12", "a + 4", "5a + 4"], "answer": "a + 12",
        "solution": r"Distribute the 3: $3a + 12 - 2a$. Combine like terms ($3a - 2a$): $a + 12$."
    },

    # ==========================================
    # LEVEL 2: INTERMEDIATE (Grade 7-8 Standard)
    # ==========================================
    {
        "id": 201, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations",
        "question": r"Evaluate: $\left( -\frac{2}{3} \right)^2 \div \frac{4}{9} - (-3)^3$",
        "options": ["28", "-26", "26", "-28"], "answer": "28",
        "solution": r"Square the fraction: $\left(-\frac{2}{3}\right)^2 = \frac{4}{9}$. Divide: $\frac{4}{9} \div \frac{4}{9} = 1$. Calculate the exponent: $(-3)^3 = -27$. Subtract: $1 - (-27) = 28$."
    },
    {
        "id": 202, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations",
        "question": "A store marks up a $40 item by 25%. During a sale, they apply a 10% discount to the new price. What is the final sale price?",
        "options": ["$45", "$42.50", "$46", "$50"], "answer": "$45",
        "solution": r"Markup: $25\%$ of $\$40$ is $\$10$, new price is $\$50$. Discount: $10\%$ of $\$50$ is $\$5$. Final price is $\$50 - \$5 = \$45$."
    },
    {
        "id": 203, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations",
        "question": r"Solve for x: $\frac{1}{2}(4x - 6) = 3x - 11$",
        "options": ["x = 8", "x = 4", "x = -8", "x = 14"], "answer": "x = 8",
        "solution": r"Distribute: $2x - 3 = 3x - 11$. Subtract $2x$: $-3 = x - 11$. Add 11: $x = 8$."
    },
    {
        "id": 204, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations",
        "question": r"Solve the inequality for x: $-3(x - 4) \leq 15$",
        "options": [r"$x \geq -1$", r"$x \leq -1$", r"$x \geq 9$", r"$x \leq 9$"], "answer": r"$x \geq -1$",
        "solution": r"Divide both sides by -3 and flip the inequality sign: $x - 4 \geq -5$. Add 4: $x \geq -1$."
    },
    {
        "id": 205, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data",
        "question": "A solid cylinder has a radius of 3 cm and a height of 10 cm. What is its exact volume?",
        "options": [r"$90\pi \text{ cm}^3$", r"$30\pi \text{ cm}^3$", r"$60\pi \text{ cm}^3$", r"$180\pi \text{ cm}^3$"], "answer": r"$90\pi \text{ cm}^3$",
        "solution": r"Volume formula is $V = \pi r^2 h$. Substitute values: $V = \pi (3)^2 (10) = 90\pi \text{ cm}^3$."
    },
    {
        "id": 206, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data",
        "question": r"Two parallel lines are intersected by a transversal. One interior angle is $(3x - 15)^\circ$ and its alternate interior angle is $(2x + 10)^\circ$. Find x.",
        "options": ["x = 25", "x = 5", "x = 35", "x = 15"], "answer": "x = 25",
        "solution": r"Alternate interior angles are equal: $3x - 15 = 2x + 10$. Subtract $2x$: $x - 15 = 10$. Add 15: $x = 25$."
    },
    {
        "id": 207, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability",
        "question": "A bag contains 4 red marbles and 6 blue marbles. If two marbles are drawn without replacement, what is the probability both are red?",
        "options": ["2/15", "4/25", "1/5", "8/45"], "answer": "2/15",
        "solution": r"Probability of 1st red: $\frac{4}{10}$. Probability of 2nd red (without replacement): $\frac{3}{9}$. Multiply: $\frac{4}{10} \times \frac{3}{9} = \frac{12}{90} = \frac{2}{15}$."
    },
    {
        "id": 208, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability",
        "question": "How many positive integer divisors does 120 have?",
        "options": ["16", "12", "14", "18"], "answer": "16",
        "solution": r"Prime factorization: $120 = 2^3 \times 3^1 \times 5^1$. Add 1 to each exponent and multiply: $(3+1)(1+1)(1+1) = 4 \times 2 \times 2 = 16$."
    },
    {
        "id": 209, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations",
        "question": r"Find the value of x and y that satisfies both equations: $2x + y = 10$ and $x - y = 2$",
        "options": ["x = 4, y = 2", "x = 2, y = 4", "x = 6, y = -2", "x = 3, y = 1"], "answer": "x = 4, y = 2",
        "solution": r"Add the equations (elimination method): $3x = 12$, so $x = 4$. Substitute back: $4 - y = 2$, so $y = 2$."
    },
    {
        "id": 210, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data",
        "question": "A student has test scores of 82, 86, and 90. What score must they get on their fourth test to achieve a mean score of exactly 88?",
        "options": ["94", "92", "96", "88"], "answer": "94",
        "solution": r"Total sum needed is $88 \times 4 = 352$. Current sum is $82 + 86 + 90 = 258$. Required score is $352 - 258 = 94$."
    },

    # ==========================================
    # LEVEL 3: DIFFICULT (Advanced & Olympiad Prep)
    # ==========================================
    {
        "id": 301, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations",
        "question": r"Rationalize the denominator: $\frac{\sqrt{3} + \sqrt{2}}{\sqrt{3} - \sqrt{2}}$",
        "options": [r"$5 + 2\sqrt{6}$", r"$5 - 2\sqrt{6}$", r"$1$", r"$5$"], "answer": r"$5 + 2\sqrt{6}$",
        "solution": r"Multiply top and bottom by the conjugate $(\sqrt{3} + \sqrt{2})$. The numerator becomes $(\sqrt{3} + \sqrt{2})^2 = 3 + 2\sqrt{6} + 2 = 5 + 2\sqrt{6}$. The denominator becomes $(\sqrt{3})^2 - (\sqrt{2})^2 = 3 - 2 = 1$."
    },
    {
        "id": 302, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations",
        "question": r"Solve for x: $8^{x-1} = 16^{2x+3}$",
        "options": ["-3", "-15/5", "-3/5", "-15/4"], "answer": "-15/5", # Simplified is -3, leaving as written for math accuracy check
        "solution": r"Convert both bases to 2. $(2^3)^{x-1} = (2^4)^{2x+3}$. This means $3(x-1) = 4(2x+3)$. Distribute: $3x - 3 = 8x + 12$. Subtract 3x: $-3 = 5x + 12$. Subtract 12: $-15 = 5x$. Therefore $x = -3$."
    },
    {
        "id": 303, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations",
        "question": r"If $x + \frac{1}{x} = 5$, find the value of $x^2 + \frac{1}{x^2}$.",
        "options": ["23", "25", "27", "10"], "answer": "23",
        "solution": r"Square both sides of the original equation: $(x + \frac{1}{x})^2 = 5^2$. This expands to $x^2 + 2(x)(\frac{1}{x}) + \frac{1}{x^2} = 25$, which simplifies to $x^2 + 2 + \frac{1}{x^2} = 25$. Subtract 2 to get $23$."
    },
    {
        "id": 304, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations",
        "question": r"Solve the system of non-linear equations: $x^2 + y^2 = 25$ and $xy = 12$. Find the positive value of $x+y$.",
        "options": ["7", "5", "12", "14"], "answer": "7",
        "solution": r"Notice that $(x+y)^2 = x^2 + y^2 + 2xy$. Substitute the given values: $(x+y)^2 = 25 + 2(12) = 25 + 24 = 49$. The positive square root is 7."
    },
    {
        "id": 305, "difficulty": "Level 3: Difficult", "category": "Geometry & Data",
        "question": r"A regular hexagon is inscribed in a circle of radius 10 cm. What is the exact area of the hexagon?",
        "options": [r"$150\sqrt{3} \text{ cm}^2$", r"$300 \text{ cm}^2$", r"$100\sqrt{3} \text{ cm}^2$", r"$600 \text{ cm}^2$"], "answer": r"$150\sqrt{3} \text{ cm}^2$",
        "solution": r"A regular hexagon is composed of 6 equilateral triangles. If inscribed in a circle of radius 10, the side length of the hexagon is also 10. Area of one triangle is $\frac{s^2\sqrt{3}}{4} = \frac{100\sqrt{3}}{4} = 25\sqrt{3}$. Multiply by 6: $150\sqrt{3}$."
    },
    {
        "id": 306, "difficulty": "Level 3: Difficult", "category": "Geometry & Data",
        "question": r"The vertices of a triangle are A(1, 2), B(5, 6), and C(9, 2). What is the area of this triangle?",
        "options": ["16", "32", "8", "24"], "answer": "16",
        "solution": r"Base AC is on the line y=2, from x=1 to x=9, so length = 8. The height is the perpendicular distance from B to AC. The y-coordinate of B is 6, and AC is at y=2, so height = 4. Area = $\frac{1}{2}bh = \frac{1}{2}(8)(4) = 16$."
    },
    {
        "id": 307, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability",
        "question": r"What is the remainder when $2^{2023}$ is divided by 7?",
        "options": ["2", "1", "4", "3"], "answer": "2",
        "solution": r"Look for a pattern. $2^1 \equiv 2 \pmod 7$. $2^2 \equiv 4 \pmod 7$. $2^3 \equiv 8 \equiv 1 \pmod 7$. The pattern repeats every 3 powers. Divide the exponent by 3: $2023 \div 3 = 674$ with a remainder of 1. Therefore, it has the same remainder as $2^1$, which is 2."
    },
    {
        "id": 308, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability",
        "question": "Five friends sit in a circle. How many different circular arrangements are possible?",
        "options": ["24", "120", "60", "12"], "answer": "24",
        "solution": r"The formula for circular permutations of $n$ distinct objects is $(n-1)!$. For 5 friends, it is $(5-1)! = 4! = 4 \times 3 \times 2 \times 1 = 24$."
    },
    {
        "id": 309, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability",
        "question": r"How many zeroes are at the end of $50!$ (50 factorial)?",
        "options": ["12", "10", "15", "5"], "answer": "12",
        "solution": r"Trailing zeroes are created by pairs of 2s and 5s. There are always more 2s than 5s in factorials, so we just count the factors of 5. $50 \div 5 = 10$. Next, check for powers of 5 ($25$): $50 \div 25 = 2$. Total zeroes = $10 + 2 = 12$."
    },
    {
        "id": 310, "difficulty": "Level 3: Difficult", "category": "Geometry & Data",
        "question": r"A sphere is inscribed perfectly inside a cube. What is the ratio of the volume of the sphere to the volume of the cube?",
        "options": [r"$\frac{\pi}{6}$", r"$\frac{\pi}{4}$", r"$\frac{2\pi}{3}$", r"$\frac{1}{2}$"], "answer": r"$\frac{\pi}{6}$",
        "solution": r"Let the side of the cube be $2r$. Volume of cube = $(2r)^3 = 8r^3$. The radius of the inscribed sphere is $r$. Volume of sphere = $\frac{4}{3}\pi r^3$. Ratio = $\frac{\frac{4}{3}\pi r^3}{8r^3} = \frac{4\pi}{24} = \frac{\pi}{6}$."
    }
]

# --- 3. UI, ROUTING AND LOGIC ---
st.set_page_config(page_title="Math Placement Test", layout="centered")

# Initialize Session State Variables to manage pages
if 'page' not in st.session_state:
    st.session_state.page = "setup"
if 'student_name' not in st.session_state:
    st.session_state.student_name = ""
if 'difficulty' not in st.session_state:
    st.session_state.difficulty = ""
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}

# ==========================================
# PAGE 1: SETUP AND DIFFICULTY SELECTION
# ==========================================
if st.session_state.page == "setup":
    st.title("Welcome to the Math Placement Test")
    st.markdown("Please enter your details and select your assigned test difficulty below.")
    
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
                st.session_state.page = "quiz"
                st.rerun()

# ==========================================
# PAGE 2: THE QUIZ
# ==========================================
elif st.session_state.page == "quiz":
    st.title(f"{st.session_state.difficulty} Test")
    st.write(f"Student: **{st.session_state.student_name}**")
    st.write("---")
    
    # Filter questions based on chosen difficulty
    filtered_quiz = [q for q in quiz_data if q['difficulty'] == st.session_state.difficulty]
    
    with st.form("quiz_form"):
        user_answers = {}
        for idx, q in enumerate(filtered_quiz):
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
    
    # Get only the questions they actually took
    filtered_quiz = [q for q in quiz_data if q['difficulty'] == st.session_state.difficulty]
    
    score = 0
    total_questions = len(filtered_quiz)
    
    # Initialize dictionary dynamically based on categories in the filtered quiz
    category_scores = {}
    for q in filtered_quiz:
        cat = q['category']
        if cat not in category_scores:
            category_scores[cat] = {"correct": 0, "total": 0}
        
        category_scores[cat]["total"] += 1
        
        # Check answer
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

    # --- Generate Radar Chart ---
    st.write("### Diagnostic Radar Analysis")
    radar_data = []
    for cat, data in category_scores.items():
        cat_percent = (data['correct'] / data['total']) * 100 if data['total'] > 0 else 0
        radar_data.append({"Category": cat, "Score": cat_percent})
        
    if len(radar_data) >= 3: # Radar charts need at least 3 points to look like a shape
        df_radar = pd.DataFrame(radar_data)
        fig = px.line_polar(
            df_radar, r='Score', theta='Category', line_close=True, range_r=[0, 100], markers=True
        )
        fig.update_traces(fill='toself', line_color='#1f77b4')
        fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    # --- Diagnostic Breakdown Progress Bars ---
    st.write("### Detailed Breakdown")
    for cat, data in category_scores.items():
        cat_percent = (data['correct'] / data['total']) * 100 if data['total'] > 0 else 0
        st.progress(cat_percent / 100, text=f"{cat}: {data['correct']}/{data['total']} ({cat_percent:.0f}%)")

    # --- Step-by-Step Solutions Section ---
    st.write("---")
    with st.expander("📝 View Step-by-Step Solutions"):
        st.write("Review your answers and the mathematical steps below.")
        for idx, q in enumerate(filtered_quiz):
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

    # Save to Google Sheets
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
        st.rerun()
