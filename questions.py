# questions.py

all_questions = [
    # ==========================================
    # LEVEL 1: EASY (Foundational Grade 7)
    # ==========================================
    
    # 1. Number Sense & Operations
    {"id": 101, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", "question": r"Evaluate the following expression by following the correct order of operations: $15 - (-4) + 3 \times 2$.", "options": ["25", "13", "11", "26"], "answer": "25", "solution": r"First, perform multiplication: $3 \times 2 = 6$. The expression becomes $15 + 4 + 6$. Summing these gives 25."},
    {"id": 102, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", "question": r"A scientist is conducting an experiment where the temperature of a liquid starts at $-12^\circ\text{C}$. The liquid is heated until it rises by exactly $25^\circ\text{C}$. What is the final temperature?", "options": ["$13^\circ\text{C}$", "$-13^\circ\text{C}$", "$37^\circ\text{C}$", "$12^\circ\text{C}$"], "answer": "$13^\circ\text{C}$", "solution": r"The calculation is $-12 + 25 = 13$."},
    {"id": 103, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", "question": r"A recipe for 4 people requires 300g of flour. If you want to make the same recipe for 10 people, how much flour is required?", "options": ["750g", "600g", "900g", "1200g"], "answer": "750g", "solution": r"Flour per person: $300 / 4 = 75\text{g}$. For 10 people: $75 \times 10 = 750\text{g}$."},
    {"id": 104, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", "question": r"Which of the following is equivalent to $0.045$?", "options": ["4.5%", "45%", "0.45%", "450%"], "answer": "4.5%", "solution": r"$0.045 \times 100 = 4.5\%$."},
    {"id": 105, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", "question": r"A library has 1,200 books. If 15% are Science Fiction and 25% are History, how many more History books are there than Science Fiction?", "options": ["120", "180", "300", "480"], "answer": "120", "solution": r"Difference is $10\%$ of 1,200, which is 120."},

    # 2. Pre-Algebra & Equations
    {"id": 106, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", "question": r"Solve for $x$: $4x + 7 = 23$.", "options": ["4", "3", "5", "6"], "answer": "4", "solution": r"$4x = 16 \rightarrow x=4$."},
    {"id": 107, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", "question": r"Simplify the expression: $3(a + 4) - 2a$.", "options": ["a + 12", "5a + 12", "a + 4", "5a + 4"], "answer": "a + 12", "solution": r"$3a + 12 - 2a = a + 12$."},
    {"id": 108, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", "question": r"If $a = 4$ and $b = -3$, find the value of $a^2 + b$.", "options": ["13", "19", "5", "1"], "answer": "13", "solution": r"$4^2 - 3 = 16 - 3 = 13$."},
    {"id": 109, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", "question": r"Solve for $y$ in the following equation: $y/4 + 6 = 10$.", "options": ["16", "4", "1", "8"], "answer": "16", "solution": r"$y/4 = 4 \rightarrow y=16$."},
    {"id": 110, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", "question": r"Simplify the expression: $2(x+3) - 3(x-1)$.", "options": ["-x + 9", "-x + 3", "x + 9", "5x + 3"], "answer": "-x + 9", "solution": r"$2x + 6 - 3x + 3 = -x + 9$."},

    # 3. Geometry & Data
    {"id": 111, "difficulty": "Level 1: Easy", "category": "Geometry & Data", "question": r"Find the area of a triangle with a base of 10 cm and a height of 6 cm.", "options": ["30 cm²", "60 cm²", "16 cm²", "120 cm²"], "answer": "30 cm²", "solution": r"$0.5 \times 10 \times 6 = 30$."},
    {"id": 112, "difficulty": "Level 1: Easy", "category": "Geometry & Data", "question": r"A square has a perimeter of 32 cm. What is its area?", "options": ["64 cm²", "32 cm²", "16 cm²", "40 cm²"], "answer": "64 cm²", "solution": r"Side = $32/4 = 8$. Area = $8^2 = 64$."},
    {"id": 113, "difficulty": "Level 1: Easy", "category": "Geometry & Data", "question": r"What is the sum of the interior angles of a regular pentagon?", "options": ["540°", "360°", "720°", "180°"], "answer": "540°", "image_svg": '''<div align="center"><svg width="100" height="100" viewBox="0 0 100 100"><polygon points="50,5 95,39 78,94 22,94 5,39" fill="none" stroke="#333" stroke-width="2"/></svg></div>''', "solution": r"$(5-2) \times 180 = 540$."},
    {"id": 114, "difficulty": "Level 1: Easy", "category": "Geometry & Data", "question": r"A triangle has two angles measuring 45° and 75°. What is the measure of the third angle?", "options": ["60°", "90°", "45°", "180°"], "answer": "60°", "solution": r"$180 - (45 + 75) = 60$."},
    {"id": 115, "difficulty": "Level 1: Easy", "category": "Geometry & Data", "question": r"Find the arithmetic mean (average) of the set: {4, 8, 12}.", "options": ["8", "24", "6", "10"], "answer": "8", "solution": r"$(4+8+12)/3 = 8$."},

    # 4. Number Theory & Probability
    {"id": 116, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", "question": r"What is the Greatest Common Factor (GCF) of 12 and 18?", "options": ["6", "2", "3", "36"], "answer": "6", "solution": r"Common factors are 1, 2, 3, 6. GCF is 6."},
    {"id": 117, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", "question": r"If you roll a fair 6-sided die, what is the probability of rolling an even number?", "options": ["1/2", "1/6", "1/3", "2/3"], "answer": "1/2", "solution": r"Even numbers are 2, 4, 6. $3/6 = 1/2$."},
    {"id": 118, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", "question": r"Which of the following is a prime number?", "options": ["17", "9", "15", "21"], "answer": "17", "solution": r"17 is only divisible by 1 and itself."},
    {"id": 119, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", "question": r"Find the Least Common Multiple (LCM) of 4 and 6.", "options": ["12", "10", "24", "2"], "answer": "12", "solution": r"Multiples of 4: 4, 8, 12. Multiples of 6: 6, 12. LCM is 12."},
    {"id": 120, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", "question": r"If a coin is flipped twice, what is the probability of getting two heads?", "options": ["1/4", "1/2", "1/8", "3/4"], "answer": "1/4", "solution": r"$1/2 \times 1/2 = 1/4$."},

    # ==========================================
    # LEVEL 2: INTERMEDIATE (Grade 8 Standard)
    # ==========================================
    
    # 1. Number Sense
    {"id": 201, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", "question": r"Simplify using index laws: $\frac{5^7 \times 5^{-3}}{5^2}$.", "options": ["25", "125", "5", "625"], "answer": "25", "solution": r"Numerator: $5^{(7-3)} = 5^4$. Divide: $5^{(4-2)} = 5^2 = 25$."},
    {"id": 202, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", "question": r"Evaluate: $\left( -\frac{2}{3} \right)^2 \div \frac{4}{9}$.", "options": ["1", "-1", "16/81", "4/9"], "answer": "1", "solution": r"$4/9 \div 4/9 = 1$."},
    {"id": 203, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", "question": r"A store marks up a $40 item by 25%. Then applies a 10% discount to the new price. Final price?", "options": ["$45", "$42.50", "$46", "$50"], "answer": "$45", "solution": r"$40 \rightarrow 50 \rightarrow 45$."},
    {"id": 204, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", "question": r"Express $0.00045$ in proper scientific notation.", "options": ["$4.5 \times 10^{-4}$", "$4.5 \times 10^{-5}$", "$45 \times 10^{-5}$", "0.45"], "answer": "$4.5 \times 10^{-4}$", "solution": r"Move decimal 4 places right."},
    {"id": 205, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", "question": r"Evaluate: $\sqrt{1.44} + (0.2)^2$.", "options": ["1.24", "1.48", "1.22", "1.64"], "answer": "1.24", "solution": r"$1.2 + 0.04 = 1.24$."},

    # 2. Pre-Algebra
    {"id": 206, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", "question": r"A rectangle has a length 3 cm longer than its width. If the perimeter is 34 cm, what is the length?", "options": ["10 cm", "7 cm", "13 cm", "17 cm"], "answer": "10 cm", "solution": r"$2(w + w+3) = 34 \rightarrow 4w+6=34 \rightarrow w=7, l=10$."},
    {"id": 207, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", "question": r"Solve for $x$: $2(x - 3) = 5x + 9$.", "options": ["-5", "-1", "5", "3"], "answer": "-5", "solution": r"$2x - 6 = 5x + 9 \rightarrow -3x = 15 \rightarrow x = -5$."},
    {"id": 208, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", "question": r"Find the slope of a line passing through (1,2) and (3,10).", "options": ["4", "2", "8", "0.25"], "answer": "4", "solution": r"$(10-2)/(3-1) = 4$."},
    {"id": 209, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", "question": r"Solve the system: $x+y=10, x-y=2$.", "options": ["6, 4", "5, 5", "7, 3", "8, 2"], "answer": "6, 4", "solution": r"$2x=12 \rightarrow x=6, y=4$."},
    {"id": 210, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", "question": r"Simplify: $(2x - 3)^2$.", "options": ["$4x^2 - 12x + 9$", "$4x^2 - 9$", "$4x^2 + 9$", "$2x^2 - 6x + 9$"], "answer": "$4x^2 - 12x + 9$", "solution": r"$(2x-3)(2x-3) = 4x^2 - 6x - 6x + 9$."},

    # 3. Geometry
    {"id": 211, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", "question": r"A ladder leans against a wall. The base is 5m from the wall and it reaches a height of 12m. How long is the ladder?", "options": ["13m", "17m", "15m", "14m"], "answer": "13m", "image_svg": '''<div align="center"><svg width="150" height="150"><line x1="20" y1="20" x2="20" y2="130" stroke="#333" stroke-width="3"/><line x1="20" y1="130" x2="130" y2="130" stroke="#333" stroke-width="3"/><line x1="20" y1="20" x2="130" y2="130" stroke="#ff4b4b" stroke-width="3" stroke-dasharray="4"/></svg></div>''', "solution": r"$\sqrt{5^2 + 12^2} = 13$."},
    {"id": 212, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", "question": r"Volume of a cylinder with radius 3m and height 7m? (use $\pi \approx 22/7$)", "options": ["198 m³", "66 m³", "462 m³", "154 m³"], "answer": "198 m³", "solution": r"$\frac{22}{7} \times 9 \times 7 = 198$."},
    {"id": 213, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", "question": r"Area of a trapezoid with bases 6 and 10 and height 4?", "options": ["32", "64", "24", "16"], "answer": "32", "solution": r"$0.5 \times (6+10) \times 4 = 32$."},
    {"id": 214, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", "question": r"Surface area of a cube with side 3?", "options": ["54", "27", "36", "9"], "answer": "54", "solution": r"$6 \times 3^2 = 54$."},
    {"id": 215, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", "question": r"In a set {10, 20, 30, 40, 100}, which is larger: mean or median?", "options": ["Mean", "Median", "They are equal", "Cannot determine"], "answer": "Mean", "solution": r"Median=30, Mean=40."},

    # 4. Number Theory
    {"id": 216, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", "question": r"How many distinct positive factors does 72 have?", "options": ["12", "10", "8", "16"], "answer": "12", "solution": r"$72 = 2^3 \times 3^2 \rightarrow (3+1)(2+1) = 12$."},
    {"id": 217, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", "question": r"What is the units digit of $3^{40}$?", "options": ["1", "3", "9", "7"], "answer": "1", "solution": r"Cycle 3,9,7,1. $40/4$ rem 0 $\rightarrow$ 1."},
    {"id": 218, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", "question": r"GCF of 84, 126, and 210?", "options": ["42", "21", "14", "6"], "answer": "42", "solution": r"All are multiples of 42."},
    {"id": 219, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", "question": r"Sum of interior angles of a convex octagon?", "options": ["1080°", "720°", "900°", "1440°"], "answer": "1080°", "solution": r"$(8-2) \times 180 = 1080$."},
    {"id": 220, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", "question": r"3-letter arrangements from {A, B, C, D, E} without repetition?", "options": ["60", "10", "15", "120"], "answer": "60", "solution": r"$5 \times 4 \times 3 = 60$."},

    # ==========================================
    # LEVEL 3: DIFFICULT (Grade 9 Competition)
    # ==========================================
    
    # 1. Number Sense
    {"id": 301, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", "question": r"Simplify the radical expression: $\sqrt{75} + \sqrt{48} - \sqrt{27}$.", "options": [r"$6\sqrt{3}$", r"$12\sqrt{3}$", r"$8\sqrt{3}$", r"$\sqrt{96}$"], "answer": r"$6\sqrt{3}$", "solution": r"$5\sqrt{3} + 4\sqrt{3} - 3\sqrt{3} = 6\sqrt{3}$."},
    {"id": 302, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", "question": r"If $x + 1/x = 5$, find the value of $x^2 + 1/x^2$.", "options": ["23", "25", "27", "10"], "answer": "23", "solution": r"$(x+1/x)^2 - 2 = 25 - 2 = 23$."},
    {"id": 303, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", "question": r"Evaluate: $8^{2/3}$.", "options": ["4", "2", "16", "8"], "answer": "4", "solution": r"$(\sqrt[3]{8})^2 = 2^2 = 4$."},
    {"id": 304, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", "question": r"Find the positive integer value of $x$: $\sqrt{6 + \sqrt{6 + \sqrt{6 + \dots}}} = x$.", "options": ["3", "2", "6", "9"], "answer": "3", "solution": r"$x^2 = 6+x \rightarrow (x-3)(x+2)=0 \rightarrow x=3$."},
    {"id": 305, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", "question": r"A car increases speed from 40 km/h to 50 km/h. Percentage increase?", "options": ["25%", "10%", "20%", "15%"], "answer": "25%", "solution": r"$(10/40) \times 100 = 25\%$."},

    # 2. Pre-Algebra
    {"id": 306, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", "question": r"Expand and simplify: $(2x - 3)(x + 4) - (x^2 - 5)$.", "options": ["$x^2 + 5x - 7$", "$x^2 + 5x + 17$", "$2x^2 + 5x - 7$", "$x^2 - 5x - 7$"], "answer": "$x^2 + 5x - 7$", "solution": r"$(2x^2+5x-12) - x^2+5 = x^2+5x-7$."},
    {"id": 307, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", "question": r"The sum of two numbers is 14 and their difference is 4. Find their product.", "options": ["45", "40", "48", "50"], "answer": "45", "solution": r"$x+y=14, x-y=4 \rightarrow x=9, y=5$. Product=45."},
    {"id": 308, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", "question": r"Solve for $x$: $8^{x-1} = 16^{2x+3}$.", "options": ["-3", "-15/5", "-3/5", "-15/4"], "answer": "-3", "solution": r"$3(x-1) = 4(2x+3) \rightarrow 3x-3=8x+12 \rightarrow -15=5x$."},
    {"id": 309, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", "question": r"Find the vertex of the parabola $y = x^2 - 4x + 7$.", "options": ["(2, 3)", "(2, 7)", "(-2, 3)", "(4, 7)"], "answer": "(2, 3)", "solution": r"$x=2, y=4-8+7=3$."},
    {"id": 310, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", "question": r"Solve $x^2 - 5x + 6 = 0$ for $x$.", "options": ["2, 3", "-2, -3", "1, 6", "0, 5"], "answer": "2, 3", "solution": r"$(x-2)(x-3)=0$."},

    # 3. Geometry
    {"id": 311, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", "question": r"Area of a regular hexagon with side length 2?", "options": ["$6\sqrt{3}$", "$12\sqrt{3}$", "$3\sqrt{3}$", "6"], "answer": "$6\sqrt{3}$", "solution": r"$6 \times (2^2 \sqrt{3}/4) = 6\sqrt{3}$."},
    {"id": 312, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", "question": r"A rectangular box has SA=94 cm². Length=4, width=3. Find height.", "options": ["5", "4", "6", "3"], "answer": "5", "solution": r"$2(12 + 4h + 3h) = 94 \rightarrow 12+7h=47 \rightarrow h=5$."},
    {"id": 313, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", "question": r"Ratio of volume of sphere to volume of circumscribed cube?", "options": [r"$\pi/6$", r"$\pi/4$", r"$2\pi/3$", r"$1/2$"], "answer": r"$\pi/6$", "solution": r"$\frac{4/3\pi r^3}{8r^3} = \pi/6$."},
    {"id": 314, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", "question": r"Distance between (1, 1) and (4, 5)?", "options": ["5", "7", "4", "25"], "answer": "5", "solution": r"$\sqrt{3^2 + 4^2} = 5$."},
    {"id": 315, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", "question": r"Interior angles of a decagon sum to?", "options": ["1440°", "1800°", "1260°", "1620°"], "answer": "1440°", "solution": r"$(10-2) \times 180 = 1440$."},

    # 4. Number Theory
    {"id": 316, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", "question": r"Smallest positive integer divisible by all integers 1 to 10?", "options": ["2520", "5040", "1260", "840"], "answer": "2520", "solution": r"LCM(1..10) = 2520."},
    {"id": 317, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", "question": r"Two dice are rolled. Prob that the sum is prime?", "options": ["5/12", "7/12", "1/2", "1/3"], "answer": "5/12", "solution": r"Sum 2,3,5,7,11 $\rightarrow$ 15 ways. $15/36 = 5/12$."},
    {"id": 318, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", "question": r
