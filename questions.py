# questions.py
all_questions = [
    # ==========================================
    # LEVEL 1: EASY (20 Questions)
    # ==========================================
    # Number Sense
    {"id": 101, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", "question": r"Evaluate the following numerical expression using the correct order of operations: $15 - (-4) + 3 \times 2$.", "options": ["25", "13", "11", "26"], "answer": "25", "solution": r"First, perform multiplication: $3 \times 2 = 6$. The expression becomes $15 + 4 + 6$. Summing these gives 25."},
    {"id": 102, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", "question": r"A student correctly answered 3 out of 5 questions on a mathematics quiz. Express this score as a percentage.", "options": ["30%", "60%", "35%", "50%"], "answer": "60%", "solution": r"Divide 3 by 5 to get 0.6. Multiply by 100 to convert the decimal to 60%."},
    {"id": 103, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", "question": r"What is the value of the exponentiation $4^3$?", "options": ["12", "16", "64", "256"], "answer": "64", "solution": r"$4^3 = 4 \times 4 \times 4$. $16 \times 4 = 64$."},
    {"id": 104, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", "question": r"A jacket originally priced at $80 is on sale for 20% off. What is the dollar amount of the discount?", "options": ["$16", "$20", "$8", "$64"], "answer": "$16", "solution": r"The discount is 20% of 80, which is $0.20 \times 80 = 16$."},
    {"id": 105, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", "question": r"Simplify the fraction $\frac{18}{24}$ to its lowest terms.", "options": ["3/4", "2/3", "4/5", "6/8"], "answer": "3/4", "solution": r"The GCF of 18 and 24 is 6. Dividing both by 6 gives 3/4."},
    # Pre-Algebra
    {"id": 106, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", "question": r"Find the value of $x$ that satisfies the linear equation: $4x + 7 = 23$.", "options": ["x = 3", "x = 4", "x = 5", "x = 6"], "answer": "x = 4", "solution": r"Subtract 7: $4x = 16$. Divide by 4: $x = 4$."},
    {"id": 107, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", "question": r"Given the linear function $y = 3x - 2$, determine the value of $y$ when $x = 5$.", "options": ["13", "15", "17", "11"], "answer": "13", "solution": r"Substitute $x=5$: $y = 3(5) - 2 = 15 - 2 = 13$."},
    {"id": 108, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", "question": r"Simplify the algebraic expression: $3(a + 4) - 2a$.", "options": ["a + 12", "5a + 12", "a + 4", "5a + 4"], "answer": "a + 12", "solution": r"$3a + 12 - 2a = a + 12$."},
    {"id": 109, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", "question": r"Solve for $x$ in the equation: $x - (-5) = 12$.", "options": ["7", "17", "-7", "12"], "answer": "7", "solution": r"$x + 5 = 12$. Subtracting 5 gives $x = 7$."},
    {"id": 110, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", "question": r"Combine the following like terms: $4x + 5y - 2x + 3y$.", "options": ["2x + 8y", "6x + 8y", "2x + 2y", "8xy"], "answer": "2x + 8y", "solution": r"$(4x - 2x) + (5y + 3y) = 2x + 8y$."},
    # Geometry
    {"id": 111, "difficulty": "Level 1: Easy", "category": "Geometry & Data", "question": r"Calculate the area of a triangle with a base of 10 cm and a height of 6 cm.", "options": ["60 cm²", "30 cm²", "16 cm²", "120 cm²"], "answer": "30 cm²", "solution": r"Area = $0.5 \times 10 \times 6 = 30$."},
    {"id": 112, "difficulty": "Level 1: Easy", "category": "Geometry & Data", "question": r"Find the perimeter of a rectangle with length 8m and width 3m.", "options": ["24m", "11m", "22m", "16m"], "answer": "22m", "solution": r"$P = 2(8+3) = 22$."},
    {"id": 113, "difficulty": "Level 1: Easy", "category": "Geometry & Data", "question": r"What is the sum of the interior angles of any triangle?", "options": ["90°", "180°", "360°", "270°"], "answer": "180°", "solution": r"By the Triangle Sum Theorem, it is always 180°."},
    {"id": 114, "difficulty": "Level 1: Easy", "category": "Geometry & Data", "question": r"A triangle has two angles of 40° and 60°. What is the third angle?", "options": ["100°", "90°", "80°", "180°"], "answer": "80°", "solution": r"$180 - (40+60) = 80$."},
    {"id": 115, "difficulty": "Level 1: Easy", "category": "Geometry & Data", "question": r"What is the arithmetic mean of 4, 8, and 12?", "options": ["8", "24", "6", "10"], "answer": "8", "solution": r"$(4+8+12) / 3 = 8$."},
    # Number Theory
    {"id": 116, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", "question": r"What is the Greatest Common Factor (GCF) of 12 and 18?", "options": ["2", "3", "6", "36"], "answer": "6", "solution": r"Factors of 12: {1,2,3,4,6,12}. Factors of 18: {1,2,3,6,9,18}. GCF is 6."},
    {"id": 117, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", "question": r"If you roll a fair 6-sided die, what is the probability of rolling an even number?", "options": ["1/6", "1/3", "1/2", "2/3"], "answer": "1/2", "solution": r"Even outcomes: {2,4,6}. Prob = 3/6 = 1/2."},
    {"id": 118, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", "question": r"Which of the following is a prime number?", "options": ["9", "15", "17", "21"], "answer": "17", "solution": r"17 is only divisible by 1 and 17."},
    {"id": 119, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", "question": r"Find the Least Common Multiple (LCM) of 4 and 6.", "options": ["10", "12", "24", "2"], "answer": "12", "solution": r"Multiples of 4: {4,8,12}. Multiples of 6: {6,12}. LCM is 12."},
    {"id": 120, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", "question": r"Probability of Heads then Tails on two fair coin flips?", "options": ["1/2", "1/4", "1/3", "1/8"], "answer": "1/4", "solution": r"$1/2 \times 1/2 = 1/4$."},

    # ==========================================
    # LEVEL 2: INTERMEDIATE (20 Questions)
    # ==========================================
    # Number Sense
    {"id": 201, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", "question": r"Evaluate: $\left( -\frac{2}{3} \right)^2 \div \frac{4}{9} - (-3)^3$.", "options": ["28", "-26", "26", "-28"], "answer": "28", "solution": r"$4/9 \div 4/9 - (-27) = 1 + 27 = 28$."},
    {"id": 202, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", "question": r"A store marks up a $40 item by 25%, then applies a 10% discount. Final price?", "options": ["\$45", "\$42.50", "\$46", "\$50"], "answer": "$45", "solution": r"Markup: $40 \rightarrow 50$. Discount: $50 \rightarrow 45$."},
    {"id": 203, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", "question": r"$(3.2 \times 10^4) \times (5 \times 10^3)$ in scientific notation?", "options": [r"$1.6 \times 10^8$", r"$16 \times 10^7$", r"$1.6 \times 10^7$", r"$8.2 \times 10^7$"], "answer": r"$1.6 \times 10^8$", "solution": r"$16 \times 10^7 = 1.6 \times 10^8$."},
    {"id": 204, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", "question": r"Simplify the complex fraction: $\frac{\frac{1}{2} + \frac{1}{3}}{\frac{1}{4}}$.", "options": ["10/3", "5/12", "12/5", "3/10"], "answer": "10/3", "solution": r"Top: 5/6. Divide by 1/4: $5/6 \times 4 = 10/3$."},
    {"id": 205, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", "question": r"Two lights flash every 18s and 24s. When do they flash together again?", "options": ["72s", "36s", "144s", "48s"], "answer": "72s", "solution": r"LCM(18, 24) = 72."},
    # Pre-Algebra
    {"id": 206, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", "question": r"Solve for $x$: $\frac{1}{2}(4x - 6) = 3x - 11$.", "options": ["x = 8", "x = 4", "x = -8", "x = 14"], "answer": "x = 8", "solution": r"$2x - 3 = 3x - 11 \rightarrow x = 8$."},
    {"id": 207, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", "question": r"Solve the inequality: $-3(x - 4) \leq 15$.", "options": [r"$x \geq -1$", r"$x \leq -1$", r"$x \geq 9$", r"$x \leq 9$"], "answer": r"$x \geq -1$", "solution": r"$x - 4 \geq -5 \rightarrow x \geq -1$."},
    {"id": 208, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", "question": r"Solve the system: $2x + y = 10$ and $x - y = 2$.", "options": ["x = 4, y = 2", "x = 2, y = 4", "x = 6, y = -2", "x = 3, y = 1"], "answer": "x = 4, y = 2", "solution": r"Add: $3x = 12 \rightarrow x=4, y=2$."},
    {"id": 209, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", "question": r"Sum of 3 consecutive even integers is 84. Largest?", "options": ["30", "28", "32", "26"], "answer": "30", "solution": r"$3x + 6 = 84 \rightarrow x=26$. Largest is 30."},
    {"id": 210, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", "question": r"Find $f(-2)$ for $f(x) = -2x^2 + 5x - 3$.", "options": ["-21", "-5", "-13", "9"], "answer": "-21", "solution": r"$-2(4) - 10 - 3 = -21$."},
    # Geometry
    {"id": 211, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", "question": r"Diagonal of rectangle 12m by 5m?", "options": ["13m", "17m", "10.9m", "14m"], "answer": "13m", "solution": r"$\sqrt{144+25} = 13$."},
    {"id": 212, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", "question": r"Volume of cylinder (r=3, h=10)?", "options": [r"$90\pi$", r"$30\pi$", r"$60\pi$", r"$180\pi$"], "answer": r"$90\pi$", "solution": r"$\pi(3^2)(10) = 90\pi$."},
    {"id": 213, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", "question": r"Find $x$ if alternate interior angles $3x-15 = 2x+10$.", "options": ["x = 25", "x = 5", "x = 35", "x = 15"], "answer": "x = 25", "solution": r"$3x - 15 = 2x + 10 \rightarrow x = 25$."},
    {"id": 214, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", "question": r"Scores: 82, 86, 90. What 4th score gives 88 mean?", "options": ["94", "92", "96", "88"], "answer": "94", "solution": r"$352 - 258 = 94$."},
    {"id": 215, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", "question": r"Area of circle with diameter 14 cm?", "options": [r"$49\pi$", r"$14\pi$", r"$196\pi$", r"$7\pi$"], "answer": r"$49\pi$", "solution": r"$\pi(7^2) = 49\pi$."},
    # Number Theory
    {"id": 216, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", "question": r"4 red, 6 blue. Prob 2 red without replacement?", "options": ["2/15", "4/25", "1/5", "8/45"], "answer": "2/15", "solution": r"$(4/10) \times (3/9) = 2/15$."},
    {"id": 217, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", "question": r"Number of divisors of 120?", "options": ["16", "12", "14", "18"], "answer": "16", "solution": r"$(3+1)(1+1)(1+1) = 16$."},
    {"id": 218, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", "question": r"Units digit of $7^{45}$?", "options": ["7", "9", "3", "1"], "answer": "7", "solution": r"Cycle: 7, 9, 3, 1. Remainder 1 = 7."},
    {"id": 219, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", "question": r"GCD of 84, 126, 210?", "options": ["42", "21", "14", "6"], "answer": "42", "solution": r"All divisible by 42."},
    {"id": 220, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", "question": r"3-letter arrangements from {A,B,C,D,E}?", "options": ["60", "10", "15", "120"], "answer": "60", "solution": r"$5 \times 4 \times 3 = 60$."},

    # ==========================================
    # LEVEL 3: DIFFICULT (20 Questions)
    # ==========================================
    # Number Sense
    {"id": 301, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", "question": r"Rationalize: $\frac{\sqrt{3} + \sqrt{2}}{\sqrt{3} - \sqrt{2}}$.", "options": [r"$5 + 2\sqrt{6}$", r"$5 - 2\sqrt{6}$", "1", "5"], "answer": r"$5 + 2\sqrt{6}$", "solution": r"Multiply by conjugate: $(\sqrt{3}+\sqrt{2})^2 = 5+2\sqrt{6}$."},
    {"id": 302, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", "question": r"Solve for $x$: $8^{x-1} = 16^{2x+3}$.", "options": ["-3", "-15/5", "-3/5", "-15/4"], "answer": "-3", "solution": r"$3(x-1) = 4(2x+3) \rightarrow x = -3$."},
    {"id": 303, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", "question": r"Simplify: $\sqrt{75} + \sqrt{48}$.", "options": [r"$9\sqrt{3}$", r"$12\sqrt{3}$", r"$8\sqrt{3}$", r"$\sqrt{123}$"], "answer": r"$9\sqrt{3}$", "solution": r"$5\sqrt{3} + 4\sqrt{3} = 9\sqrt{3}$."},
    {"id": 304, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", "question": r"Evaluate $\log_2(32)$.", "options": ["5", "4", "6", "16"], "answer": "5", "solution": r"$2^5 = 32$."},
    {"id": 305, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", "question": r"Sum of infinite series: $1 + 1/2 + 1/4 ...$", "options": ["2", "1.5", "Inf", "4"], "answer": "2", "solution": r"$a/(1-r) = 1/(0.5) = 2$."},
    # Pre-Algebra
    {"id": 306, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", "question": r"If $x + 1/x = 5$, find $x^2 + 1/x^2$.", "options": ["23", "25", "27", "10"], "answer": "23", "solution": r"$(x+1/x)^2 - 2 = 25 - 2 = 23$."},
    {"id": 307, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", "question": r"Solve $x^2 + y^2 = 25, xy = 12$ for positive $(x+y)$.", "options": ["7", "5", "12", "14"], "answer": "7", "solution": r"$\sqrt{25+24} = 7$."},
    {"id": 308, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", "question": r"Roots of $x^2 - 5x + 6 = 0$?", "options": ["2, 3", "-2, -3", "1, 6", "-1, -6"], "answer": "2, 3", "solution": r"$(x-2)(x-3)=0$."},
    {"id": 309, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", "question": r"Vertex of $y = x^2 - 4x + 3$?", "options": ["(2, -1)", "(-2, 1)", "(4, 3)", "(0, 3)"], "answer": "(2, -1)", "solution": r"$x=2, y=4-8+3=-1$."},
    {"id": 310, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", "question": r"Domain of $1/\sqrt{x-3}$?", "options": [r"$x > 3$", r"$x \geq 3$", r"$x \neq 3$", "All"], "answer": r"$x > 3$", "solution": r"$x-3 > 0 \rightarrow x > 3$."},
    # Geometry
    {"id": 311, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", "question": r"Hexagon in circle radius 10. Area?", "options": [r"$150\sqrt{3}$", r"$300$", r"$100\sqrt{3}$", r"$600$"], "answer": r"$150\sqrt{3}$", "solution": r"$6 \times (25\sqrt{3}) = 150\sqrt{3}$."},
    {"id": 312, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", "question": r"Triangle A(1,2), B(5,6), C(9,2). Area?", "options": ["16", "32", "8", "24"], "answer": "16", "solution": r"$0.5 \times 8 \times 4 = 16$."},
    {"id": 313, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", "question": r"Sphere in cube ratio of Vol?", "options": [r"$\pi/6$", r"$\pi/4$", r"$2\pi/3$", r"$1/2$"], "answer": r"$\pi/6$", "solution": r"$\frac{4/3\pi r^3}{8r^3} = \pi/6$."},
    {"id": 314, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", "question": r"Arc length 60° radius 6?", "options": [r"$2\pi$", r"$4\pi$", r"$\pi$", r"$6\pi$"], "answer": r"$2\pi$", "solution": r"$(1/6) \times 12\pi = 2\pi$."},
    {"id": 315, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", "question": r"Distance (-2,4) to (4,-4)?", "options": ["10", "14", "8", "100"], "answer": "10", "solution": r"$\sqrt{36+64} = 10$."},
    # Number Theory
    {"id": 316, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", "question": r"Remainder $2^{2023} \div 7$?", "options": ["2", "1", "4", "3"], "answer": "2", "solution": r"Cycle mod 7 is 2,4,1. Remainder 1 = 2."},
    {"id": 317, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", "question": r"5 in circle arrangements?", "options": ["24", "120", "60", "12"], "answer": "24", "solution": r"$(5-1)! = 24$."},
    {"id": 318, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", "question": r"Zeroes at end of 50!?", "options": ["12", "10", "15", "5"], "answer": "12", "solution": r"$10 + 2 = 12$."},
    {"id": 319, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", "question": r"Prob 2 dice sum prime?", "options": ["5/12", "7/18", "1/3", "1/4"], "answer": "5/12", "solution": r"15/36 = 5/12."},
    {"id": 320, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", "question": r"10 Choose 3 students?", "options": ["120", "720", "30", "1000"], "answer": "120", "solution": r"$(10 \times 9 \times 8) / 6 = 120$."}
]
