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

# --- 2. QUIZ DATA, SYLLABUS & SOLUTIONS ---
quiz_data = [
    # Number Sense & Operations
    {
        "id": 1,
        "category": "Number Sense & Operations",
        "question": r"Evaluate: $\left( -\frac{2}{3} \right)^2 \div \frac{4}{9} - (-3)^3$",
        "options": ["28", "-26", "26", "-28"],
        "answer": "28",
        "solution": r"First, square the fraction: $\left(-\frac{2}{3}\right)^2 = \frac{4}{9}$. Next, divide: $\frac{4}{9} \div \frac{4}{9} = 1$. Then, calculate the exponent: $(-3)^3 = -27$. Finally, subtract: $1 - (-27) = 1 + 27 = 28$."
    },
    {
        "id": 2,
        "category": "Number Sense & Operations",
        "question": "A store marks up a $40 item by 25%. During a sale, they apply a 10% discount to the new price. What is the final sale price?",
        "options": ["$45", "$42.50", "$46", "$50"],
        "answer": "$45",
        "solution": r"First, find the markup: $25\%$ of $\$40$ is $\$10$, making the new price $\$50$. Next, calculate the $10\%$ discount on the new price: $10\%$ of $\$50$ is $\$5$. The final price is $\$50 - \$5 = \$45$."
    },
    {
        "id": 3,
        "category": "Number Sense & Operations",
        "question": r"Calculate the product and express in scientific notation: $(3.2 \times 10^4) \times (5 \times 10^3)$",
        "options": [r"$1.6 \times 10^8$", r"$16 \times 10^7$", r"$1.6 \times 10^7$", r"$8.2 \times 10^7$"],
        "answer": r"$1.6 \times 10^8$",
        "solution": r"Multiply the decimals: $3.2 \times 5 = 16$. Multiply the powers of 10 by adding exponents: $10^4 \times 10^3 = 10^7$. The result is $16 \times 10^7$. To convert to proper scientific notation, move the decimal one place left and increase the exponent: $1.6 \times 10^8$."
    },
    {
        "id": 4,
        "category": "Number Sense & Operations",
        "question": r"Simplify the complex fraction: $\frac{\frac{1}{2} + \frac{1}{3}}{\frac{1}{4}}$",
        "options": ["10/3", "5/12", "12/5", "3/10"],
        "answer": "10/3",
        "solution": r"First, find a common denominator for the top fractions: $\frac{3}{6} + \frac{2}{6} = \frac{5}{6}$. The problem is now $\frac{5}{6} \div \frac{1}{4}$. To divide fractions, multiply by the reciprocal: $\frac{5}{6} \times \frac{4}{1} = \frac{20}{6}$. Simplify the fraction to $\frac{10}{3}$."
    },
    {
        "id": 5,
        "category": "Number Sense & Operations",
        "question": "Two flashing warning lights turn on at the exact same time. Light A flashes every 18 seconds, and Light B flashes every 24 seconds. How many seconds will pass before they flash together again?",
        "options": ["72 seconds", "36 seconds", "144 seconds", "48 seconds"],
        "answer": "72 seconds",
        "solution": r"This problem asks for the Least Common Multiple (LCM) of $18$ and $24$. The multiples of $18$ are $18, 36, 54, 72, 90...$ The multiples of $24$ are $24, 48, 72...$ The smallest common multiple is $72$."
    },
    
    # Pre-Algebra & Equations
    {
        "id": 6,
        "category": "Pre-Algebra & Equations",
        "question": r"Solve for x: $\frac{1}{2}(4x - 6) = 3x - 11$",
        "options": ["x = 8", "x = 4", "x = -8", "x = 14"],
        "answer": "x = 8",
        "solution": r"Distribute the $\frac{1}{2}$ on the left side: $2x - 3 = 3x - 11$. Subtract $2x$ from both sides: $-3 = x - 11$. Add $11$ to both sides to isolate $x$: $8 = x$."
    },
    {
        "id": 7,
        "category": "Pre-Algebra & Equations",
        "question": r"Solve the inequality for x: $-3(x - 4) \leq 15$",
        "options": [r"$x \geq -1$", r"$x \leq -1$", r"$x \geq 9$", r"$x \leq 9$"],
        "answer": r"$x \geq -1$",
        "solution": r"Divide both sides by $-3$. **Crucial rule:** When dividing an inequality by a negative number, you must flip the inequality sign. The equation becomes $x - 4 \geq -5$. Add $4$ to both sides: $x \geq -1$."
    },
    {
        "id": 8,
        "category": "Pre-Algebra & Equations",
        "question": r"Find the value of x and y that satisfies both equations: $2x + y = 10$ and $x - y = 2$",
        "options": ["x = 4, y = 2", "x = 2, y = 4", "x = 6, y = -2", "x = 3, y = 1"],
        "answer": "x = 4, y = 2",
        "solution": r"Use the elimination method. Add the two equations together: $(2x + x) + (y - y) = (10 + 2)$. This simplifies to $3x = 12$, so $x = 4$. Substitute $x=4$ back into the second equation: $4 - y = 2$, which means $y = 2$."
    },
    {
        "id": 9,
        "category": "Pre-Algebra & Equations",
        "question": "The sum of three consecutive even integers is 84. What is the largest of these three integers?",
        "options": ["30", "28", "32", "26"],
        "answer": "30",
        "solution": r"Let the first even integer be $x$. The next consecutive even integers are $(x+2)$ and $(x+4)$. The equation is $x + (x+2) + (x+4) = 84$. Combine like terms: $3x + 6 = 84$. Subtract $6$: $3x = 78$. Divide by $3$: $x = 26$. The largest integer is $x + 4 = 26 + 4 = 30$."
    },
    {
        "id": 10,
        "category": "Pre-Algebra & Equations",
        "question": r"If $f(x) = -2x^2 + 5x - 3$, find the value of $f(-2)$.",
        "options": ["-21", "-5", "-13", "9"],
        "answer": "-21",
        "solution": r"Substitute $-2$ wherever there is an $x$: $f(-2) = -2(-2)^2 + 5(-2) - 3$. Exponents first: $(-2)^2 = 4$. Now multiply: $-2(4) + (-10) - 3$. This becomes $-8 - 10 - 3$, which equals $-21$."
    },

    # Geometry & Data
    {
        "id": 11,
        "category": "Geometry & Data",
        "question": "A rectangular garden is 12 meters long and 5 meters wide. What is the exact length of a straight diagonal path connecting two opposite corners?",
        "options": ["13 meters", "17 meters", "10.9 meters", "14 meters"],
        "answer": "13 meters",
        "image_svg": '''
        <div align="center">
        <svg width="250" height="130" xmlns="http://www.w3.org/2000/svg">
          <rect x="25" y="20" width="200" height="80" fill="#f0f8ff" stroke="#333" stroke-width="2"/>
          <line x1="25" y1="100" x2="225" y2="20" stroke="#ff4b4b" stroke-width="2" stroke-dasharray="5,5"/>
          <text x="110" y="118" font-family="sans-serif" font-size="14" font-weight="bold" fill="#333">12 m</text>
          <text x="0" y="65" font-family="sans-serif" font-size="14" font-weight="bold" fill="#333">5 m</text>
        </svg>
        </div>
        ''',
        "solution": r"Use the Pythagorean theorem ($a^2 + b^2 = c^2$) where the diagonal is the hypotenuse ($c$). $5^2 + 12^2 = c^2$. $25 + 144 = c^2$. $169 = c^2$. The square root of $169$ is $13$."
    },
    {
        "id": 12,
        "category": "Geometry & Data",
        "question": "A solid cylinder has a radius of 3 cm and a height of 10 cm. What is its exact volume?",
        "options": [r"$90\pi \text{ cm}^3$", r"$30\pi \text{ cm}^3$", r"$60\pi \text{ cm}^3$", r"$180\pi \text{ cm}^3$"],
        "answer": r"$90\pi \text{ cm}^3$",
        "image_svg": '''
        <div align="center">
        <svg width="150" height="180" xmlns="http://www.w3.org/2000/svg">
          <ellipse cx="75" cy="30" rx="50" ry="15" fill="#e6f2ff" stroke="#333" stroke-width="2"/>
          <ellipse cx="75" cy="150" rx="50" ry="15" fill="#f0f8ff" stroke="#333" stroke-width="2"/>
          <line x1="25" y1="30" x2="25" y2="150" stroke="#333" stroke-width="2"/>
          <line x1="125" y1="30" x2="125" y2="150" stroke="#333" stroke-width="2"/>
          <line x1="75" y1="30" x2="125" y2="30" stroke="#ff4b4b" stroke-width="2" stroke-dasharray="4,4"/>
          <circle cx="75" cy="30" r="3" fill="#333"/>
          <text x="85" y="25" font-family="sans-serif" font-size="14" font-weight="bold" fill="#ff4b4b">r = 3</text>
          <text x="130" y="95" font-family="sans-serif" font-size="14" font-weight="bold" fill="#333">h = 10</text>
        </svg>
        </div>
        ''',
        "solution": r"The volume formula for a cylinder is $V = \pi r^2 h$. Substitute the given values: $V = \pi (3)^2 (10)$. Calculate the radius squared: $3^2 = 9$. Multiply by the height: $9 \times 10 = 90$. The exact volume is $90\pi \text{ cm}^3$."
    },
    {
        "id": 13,
        "category": "Geometry & Data",
        "question": r"Two parallel lines are intersected by a transversal line. If one interior angle measures $(3x - 15)^\circ$ and its alternate interior angle measures $(2x + 10)^\circ$, find the value of x.",
        "options": ["x = 25", "x = 5", "x = 35", "x = 15"],
        "answer": "x = 25",
        "image_svg": '''
        <div align="center">
        <svg width="250" height="150" xmlns="http://www.w3.org/2000/svg">
          <line x1="20" y1="40" x2="230" y2="40" stroke="#333" stroke-width="2"/>
          <line x1="20" y1="110" x2="230" y2="110" stroke="#333" stroke-width="2"/>
          <line x1="60" y1="140" x2="190" y2="10" stroke="#ff4b4b" stroke-width="2"/>
          
          <path d="M 140 40 A 20 20 0 0 0 130 55" fill="none" stroke="#ff4b4b" stroke-width="2"/>
          <path d="M 110 110 A 20 20 0 0 0 120 95" fill="none" stroke="#ff4b4b" stroke-width="2"/>
          
          <text x="65" y="60" font-family="sans-serif" font-size="14" font-weight="bold" fill="#333">(3x - 15)°</text>
          <text x="125" y="90" font-family="sans-serif" font-size="14" font-weight="bold" fill="#333">(2x + 10)°</text>
        </svg>
        </div>
        ''',
        "solution": r"Alternate interior angles are equal when lines are parallel. Set the equations equal to each other: $3x - 15 = 2x + 10$. Subtract $2x$ from both sides: $x - 15 = 10$. Add $15$ to both sides: $x = 25$."
    },
    {
        "id": 14,
        "category": "Geometry & Data",
        "question": "A student has test scores of 82, 86, and 90. What score must they get on their fourth test to achieve a mean score of exactly 88?",
        "options": ["94", "92", "96", "88"],
        "answer": "94",
        "solution": r"To average an $88$ across $4$ tests, the total sum of all scores must be $88 \times 4 = 352$. The sum of the first three tests is $82 + 86 + 90 = 258$. The required score for the fourth test is $352 - 258 = 94$."
    },
    
    # Number Theory & Probability
    {
        "id": 15,
        "category": "Number Theory & Probability",
        "question": "A bag contains 4 red marbles and 6 blue marbles. If two marbles are drawn at random without replacement, what is the probability that both drawn marbles are red?",
        "options": ["2/15", "4/25", "1/5", "8/45"],
        "answer": "2/15",
        "solution": r"There are $10$ total marbles. The probability of the first marble being red is $\frac{4}{10}$. Because it is NOT replaced, there are now $3$ red marbles left out of $9$ total marbles. The probability of the second marble being red is $\frac{3}{9}$. Multiply the probabilities: $\frac{4}{10} \times \frac{3}{9} = \frac{12}{90}$. Simplify the fraction to $\frac{2}{15}$."
    },
    {
        "id": 16,
        "category": "Number Theory & Probability",
        "question": "How many positive integer divisors does 120 have?",
        "options": ["16", "12", "14", "18"],
        "answer": "16",
        "solution": r"First, find the prime factorization of $120$: $120 = 8 \times 15 = 2^3 \times 3^1 \times 5^1$. To find the total number of divisors, add $1$ to each of the exponents and multiply them together: $(3+1) \times (1+1) \times (1+1) = 4 \times 2 \times 2 = 16$."
    },
    {
        "id": 17,
        "category": "Number Theory & Probability",
        "question": r"What is the units digit of $7^{45}$?",
        "options": ["7", "9", "3", "1"],
        "answer": "7",
        "solution": r"The units digits of powers of $7$ repeat in a cycle of four: $7^1 \rightarrow 7$, $7^2 \rightarrow 9$, $7^3 \rightarrow 3$, $7^4 \rightarrow 1$. To find the digit for $7^{45}$, divide the exponent by $4$: $45 \div 4 = 11$ with a remainder of $1$. A remainder of $1$ means it is the first number in the cycle, which is $7$."
    },
    {
        "id": 18,
        "category": "Number Theory & Probability",
        "question": "A teacher has 84 red pens, 126 blue pens, and 210 black pens. They want to pack them into identical boxes such that each box has the same combination of pens with none left over. What is the greatest number of boxes they can pack?",
        "options": ["42", "21", "14", "6"],
        "answer": "42",
        "solution": r"This asks for the Greatest Common Divisor (GCD) of $84$, $126$, and $210$. Notice that all numbers are multiples of $42$: $84 = 42 \times 2$, $126 = 42 \times 3$, and $210 = 42 \times 5$. Since $2, 3,$ and $5$ share no common factors, the greatest common divisor is $42$."
    },
    {
        "id": 19,
        "category": "Number Theory & Probability",
        "question": "Using the letters A, B, C, D, and E, how many different 3-letter arrangements can be formed if no letter is repeated?",
        "options": ["60", "10", "15", "120"],
        "answer": "60",
        "solution": r"This is a permutation problem. You have $5$ choices for the first letter. Once chosen, you have $4$ choices for the second letter. Once chosen, you have $3$ choices for the third letter. Multiply the possibilities: $5 \times 4 \times 3 = 60$ arrangements."
    },
    {
        "id": 20,
        "category": "Number Theory & Probability",
        "question": "Two fair six-sided dice are rolled simultaneously. What is the probability that the sum of the numbers rolled is a prime number?",
        "options": ["5/12", "7/18", "1/3", "1/4"],
        "answer": "5/12",
        "solution": r"There are $36$ total possible outcomes ($6 \times 6$). The possible prime sums are $2, 3, 5, 7,$ and $11$. Number of ways to roll a $2$ (1 way). Roll a $3$ (2 ways). Roll a $5$ (4 ways). Roll a $7$ (6 ways). Roll an $11$ (2 ways). Total prime rolls: $1 + 2 + 4 + 6 + 2 = 15$. The probability is $\frac{15}{36}$, which simplifies to $\frac{5}{12}$."
    }
]

# --- 3. UI AND LOGIC ---
st.set_page_config(page_title="Grade 7-8 Math Placement", layout="centered")

st.title("Grade 7-8 Advanced Math Placement Test")
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
            
            # --> NEW: Check for an SVG image and draw it if it exists!
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
            if not student_name:
                st.error("Please enter your name before submitting.")
            else:
                st.session_state.student_name = student_name
                st.session_state.user_answers = user_answers
                st.session_state.submitted = True
                st.rerun()

# --- 4. EVALUATION, REPORTING & SOLUTIONS ---
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

    # --- Step-by-Step Solutions Section ---
    st.write("---")
    with st.expander("📝 View Step-by-Step Solutions"):
        st.write("Review your answers and the mathematical steps below.")
        for idx, q in enumerate(quiz_data):
            user_ans = st.session_state.user_answers[q['id']]
            correct_ans = q['answer']
            
            if user_ans == correct_ans:
                status_icon = "✅"
                st.markdown(f"**Q{idx+1}. {status_icon} Correct**")
            else:
                status_icon = "❌"
                st.markdown(f"**Q{idx+1}. {status_icon} Incorrect** (You chose: {user_ans})")
            
            st.markdown(f"**Question:** {q['question']}")
            
            # Show the picture again in the solutions!
            if "image_svg" in q:
                st.markdown(q["image_svg"], unsafe_allow_html=True)
                
            st.markdown(f"**Correct Answer:** {correct_ans}")
            st.info(f"**Solution:** {q['solution']}")
            st.write("")

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
