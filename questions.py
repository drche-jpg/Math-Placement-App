# questions.py

all_questions = [
    # ==========================================
    # LEVEL 1: EASY (Foundational Competition)
    # ==========================================
    {"id": 101, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", 
     "question": r"In a specific mathematical sequence, the value of a term is found by squaring the previous term and then subtracting 5. If the first term is 3, determine the exact value of the third term in this sequence.", 
     "options": ["11", "4", "16", "21"], "answer": "11", 
     "solution": r"Term 1 = 3. Term 2 = $3^2 - 5 = 4$. Term 3 = $4^2 - 5 = 11$."},
    
    {"id": 102, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", 
     "question": r"A standard six-sided die is rolled twice. What is the probability that the sum of the two numbers rolled is exactly 5?", 
     "options": ["1/9", "1/6", "4/36", "1/12"], "answer": "1/9", 
     "solution": r"Possible pairs $(a,b)$ that sum to 5 are (1,4), (2,3), (3,2), and (4,1). Total outcomes = 36. Probability = $4/36 = 1/9$."},

    {"id": 103, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", 
     "question": r"The sum of three consecutive integers is 72. What is the value of the largest of these three integers?", 
     "options": ["25", "23", "24", "26"], "answer": "25", 
     "solution": r"Let the integers be $n-1, n, n+1$. The sum is $3n = 72$, so $n = 24$. The largest is $24 + 1 = 25$."},

    {"id": 104, "difficulty": "Level 1: Easy", "category": "Geometry & Data", 
     "question": r"A square has a perimeter of 32 cm. If a rectangle is constructed with the same area as the square and has a width of 4 cm, what is the perimeter of this rectangle?", 
     "options": ["40 cm", "20 cm", "32 cm", "44 cm"], "answer": "40 cm",
     "image_svg": '''<div align="center"><svg width="200" height="100" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="10" width="80" height="80" fill="none" stroke="#333" stroke-width="2"/><rect x="110" y="30" width="80" height="40" fill="none" stroke="#ff4b4b" stroke-width="2"/><text x="35" y="105" font-size="12">Square</text><text x="125" y="105" font-size="12">Rectangle</text></svg></div>''',
     "solution": r"Square side = $32/4 = 8$. Area = $8^2 = 64$. Rectangle length = $64/4 = 16$. Perimeter = $2(16+4) = 40$."},

    {"id": 105, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", 
     "question": r"A library is organizing 1,200 books. If 15% are Science Fiction and 25% are History, how many more History books are there than Science Fiction books?", 
     "options": ["120", "180", "300", "480"], "answer": "120", 
     "solution": r"Percentage difference = $25\% - 15\% = 10\%$. $10\%$ of 1,200 = 120."},

    {"id": 106, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", "question": r"Solve for $x$: $5(x - 2) = 3(x + 4)$.", "options": ["11", "1", "22", "5"], "answer": "11", "solution": r"$5x - 10 = 3x + 12 \rightarrow 2x = 22 \rightarrow x = 11$."},
    {"id": 107, "difficulty": "Level 1: Easy", "category": "Geometry & Data", "question": r"Calculate the mean of the data set: {14, 22, 18, 30, 16}.", "options": ["20", "18", "22", "25"], "answer": "20", "solution": r"Sum = 100. $100 / 5 = 20$."},
    {"id": 108, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", "question": r"What is the GCF of 48 and 72?", "options": ["24", "12", "6", "36"], "answer": "24", "solution": r"Factors of 48: 1..24,48. Factors of 72: 1..24,36,72. GCF is 24."},
    {"id": 109, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", "question": r"Evaluate $3.5 \times 1.2 + 4.8 \div 0.6$.", "options": ["12.2", "9", "13", "11.2"], "answer": "12.2", "solution": r"$4.2 + 8 = 12.2$."},
    {"id": 110, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", "question": r"If $a=3$ and $b=-2$, find $2a^2 - 3b$.", "options": ["24", "12", "30", "18"], "answer": "24", "solution": r"$2(9) - 3(-2) = 18 + 6 = 24$."},
    {"id": 111, "difficulty": "Level 1: Easy", "category": "Geometry & Data", "question": r"Area of a circle with radius 7 (use $\pi \approx 22/7$)?", "options": ["154", "44", "49", "144"], "answer": "154", "solution": r"$\pi(49) \approx 154$."},
    {"id": 112, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", "question": r"How many prime numbers are between 1 and 20?", "options": ["8", "7", "9", "10"], "answer": "8", "solution": r"2, 3, 5, 7, 11, 13, 17, 19."},
    {"id": 113, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", "question": r"Simplify: $2^4 - 3^2 + 5^0$.", "options": ["8", "7", "12", "1"], "answer": "8", "solution": r"$16 - 9 + 1 = 8$."},
    {"id": 114, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", "question": r"Solve for $y$: $y/4 + 6 = 10$.", "options": ["16", "4", "1", "8"], "answer": "16", "solution": r"$y/4 = 4 \rightarrow y=16$."},
    {"id": 115, "difficulty": "Level 1: Easy", "category": "Geometry & Data", "question": r"A triangle has angles 45° and 75°. Third angle?", "options": ["60°", "90°", "45°", "180°"], "answer": "60°", "solution": r"$180 - 120 = 60$."},
    {"id": 116, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", "question": r"LCM of 15 and 20?", "options": ["60", "30", "300", "5"], "answer": "60", "solution": r"Multiples of 15: 15,30,45,60. 20: 20,40,60."},
    {"id": 117, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", "question": r"What is 0.4% of 500?", "options": ["2", "20", "200", "0.2"], "answer": "2", "solution": r"$0.004 \times 500 = 2$."},
    {"id": 118, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", "question": r"Simplify: $2(x+3) - 3(x-1)$.", "options": ["-x + 9", "-x + 3", "x + 9", "5x + 3"], "answer": "-x + 9", "solution": r"$2x+6 - 3x+3 = -x+9$."},
    {"id": 119, "difficulty": "Level 1: Easy", "category": "Geometry & Data", "question": r"A cube has a volume of 27. Surface area?", "options": ["54", "36", "9", "27"], "answer": "54", "solution": r"Side = 3. $SA = 6(3^2) = 54$."},
    {"id": 120, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", "question": r"Draw one card from 52. Prob of Ace?", "options": ["1/13", "1/52", "1/4", "4/13"], "answer": "1/13", "solution": r"$4/52 = 1/13$."},

    # ==========================================
    # LEVEL 2: INTERMEDIATE (20 Questions)
    # ==========================================
    {"id": 201, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", 
     "question": r"Evaluate the following expression by applying the laws of exponents: $\frac{2^5 \times 3^4}{2^3 \times 3^2} - \sqrt{144}$.", 
     "options": ["24", "36", "12", "48"], "answer": "24", 
     "solution": r"Simplify exponents: $2^{(5-3)} \times 3^{(4-2)} = 2^2 \times 3^2 = 4 \times 9 = 36$. Since $\sqrt{144} = 12$, $36 - 12 = 24$."},

    {"id": 202, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", 
     "question": r"How many distinct positive factors does the number 72 have?", 
     "options": ["12", "10", "8", "16"], "answer": "12", 
     "solution": r"Prime factorization: $72 = 2^3 \times 3^2$. Number of factors = $(3+1)(2+1) = 4 \times 3 = 12$."},

    {"id": 203, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", 
     "question": r"A taxi company charges a base fee of $5.00 plus $2.50 per mile. If a passenger's total fare was $35.00, how many miles did they travel?", 
     "options": ["12", "14", "10", "15"], "answer": "12", 
     "solution": r"Equation: $5 + 2.5m = 35 \rightarrow 2.5m = 30 \rightarrow m = 12$."},

    {"id": 204, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", 
     "question": r"A cylindrical water tank has a radius of 3 meters and a height of 7 meters. Using $\pi \approx \frac{22}{7}$, calculate the total volume of the tank in cubic meters.", 
     "options": ["198", "66", "462", "154"], "answer": "198",
     "image_svg": '''<div align="center"><svg width="100" height="120" xmlns="http://www.w3.org/2000/svg"><ellipse cx="50" cy="20" rx="30" ry="10" fill="none" stroke="#333"/><line x1="20" y1="20" x2="20" y2="100" stroke="#333"/><line x1="80" y1="20" x2="80" y2="100" stroke="#333"/><ellipse cx="50" cy="100" rx="30" ry="10" fill="none" stroke="#333" stroke-dasharray="2,2"/></svg></div>''',
     "solution": r"Volume = $\pi r^2 h = \frac{22}{7} \times 3^2 \times 7 = 22 \times 9 = 198$."},

    {"id": 205, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", "question": r"Simplify: $(1/2 + 1/3) / (1/4)$.", "options": ["10/3", "5/12", "1/6", "2"], "answer": "10/3", "solution": r"$5/6 \times 4 = 20/6 = 10/3$."},
    {"id": 206, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", "question": r"Solve for $x$: $x^2 - 5x + 6 = 0$.", "options": ["2, 3", "-2, -3", "1, 6", "0, 5"], "answer": "2, 3", "solution": r"$(x-2)(x-3)=0$."},
    {"id": 207, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", "question": r"Find the hypotenuse of a right triangle with legs 5 and 12.", "options": ["13", "17", "15", "11"], "answer": "13", "solution": r"$\sqrt{25+144} = 13$."},
    {"id": 208, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", "question": r"Probability of drawing a King or Queen from 52 cards?", "options": ["2/13", "1/13", "4/13", "1/26"], "answer": "2/13", "solution": r"$8/52 = 2/13$."},
    {"id": 209, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", "question": r"Express 0.00045 in scientific notation.", "options": ["$4.5 \times 10^{-4}$", "$4.5 \times 10^{-5}$", "$45 \times 10^{-5}$", "0.45"], "answer": "$4.5 \times 10^{-4}$", "solution": r"Move decimal 4 places right."},
    {"id": 210, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", "question": r"Solve system: $x+y=10, x-y=2$.", "options": ["6, 4", "5, 5", "7, 3", "8, 2"], "answer": "6, 4", "solution": r"$2x=12 \rightarrow x=6, y=4$."},
    {"id": 211, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", "question": r"Interior angle of a regular hexagon?", "options": ["120°", "108°", "90°", "135°"], "answer": "120°", "solution": r"$(6-2) \times 180 / 6 = 120$."},
    {"id": 212, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", "question": r"What is the units digit of $3^{40}$?", "options": ["1", "3", "9", "7"], "answer": "1", "solution": r"Cycle 3,9,7,1. $40 \div 4 = 10$ R 0."},
    {"id": 213, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", "question": r"Evaluate: $2.5^2 - 1.5^2$.", "options": ["4", "5", "6.25", "1"], "answer": "4", "solution": r"$6.25 - 2.25 = 4$."},
    {"id": 214, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", "question": r"If $f(x) = 3x-5$, find $f(f(2))$.", "options": ["-2", "1", "2", "-5"], "answer": "-2", "solution": r"$f(2)=1, f(1)=-2$."},
    {"id": 215, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", "question": r"Area of equilateral triangle with side 4?", "options": ["$4\sqrt{3}$", "8", "$8\sqrt{3}$", "4"], "answer": "$4\sqrt{3}$", "solution": r"$s^2\sqrt{3}/4 = 16\sqrt{3}/4$."},
    {"id": 216, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", "question": r"How many integers between 1 and 100 are divisible by 3 and 5?", "options": ["6", "5", "7", "10"], "answer": "6", "solution": r"Divisible by 15: 15,30,45,60,75,90."},
    {"id": 217, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", "question": r"Simplify: $\sqrt{72} / \sqrt{2}$.", "options": ["6", "36", "12", "18"], "answer": "6", "solution": r"$\sqrt{36} = 6$."},
    {"id": 218, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", "question": r"Slope of line $2x + 3y = 6$?", "options": ["-2/3", "2/3", "-2", "2"], "answer": "-2/3", "solution": r"$3y = -2x+6 \rightarrow y = -2/3x+2$."},
    {"id": 219, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", "question": r"Volume of sphere radius 3?", "options": ["$36\pi$", "$12\pi$", "$9\pi$", "$27\pi$"], "answer": "$36\pi$", "solution": r"$4/3\pi(27) = 36\pi$."},
    {"id": 220, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", "question": r"Sum of interior angles of an octagon?", "options": ["1080°", "720°", "900°", "1440°"], "answer": "1080°", "solution": r"$(8-2) \times 180 = 1080$."},

    # ==========================================
    # LEVEL 3: DIFFICULT (20 Questions)
    # ==========================================
    {"id": 301, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", 
     "question": r"Consider the infinite nested radical $x = \sqrt{6 + \sqrt{6 + \sqrt{6 + \dots}}}$. Determine the positive integer value of $x$.", 
     "options": ["3", "2", "6", "9"], "answer": "3", 
     "solution": r"Let $x = \sqrt{6+x} \rightarrow x^2 - x - 6 = 0 \rightarrow (x-3)(x+2) = 0$. Positive $x=3$."},

    {"id": 302, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", 
     "question": r"What is the remainder when $2^{2026}$ is divided by 7?", 
     "options": ["2", "4", "1", "0"], "answer": "2", 
     "solution": r"Cycle of $2^n \pmod 7$: $2, 4, 1, 2, 4, 1 \dots$ (period 3). $2026 = 3 \times 675 + 1$. Same as $2^1 \pmod 7 = 2$."},

    {"id": 303, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", 
     "question": r"In a group of 30 students, 18 play soccer, 15 play basketball, and 5 play neither. How many students play BOTH soccer and basketball?", 
     "options": ["8", "10", "5", "12"], "answer": "8", 
     "solution": r"Total playing sports = $30 - 5 = 25$. Both = $(18 + 15) - 25 = 8$."},

    {"id": 304, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", 
     "question": r"Two parallel lines are intersected by a transversal. If alternate interior angles measure $(3x - 15)^\circ$ and $(2x + 10)^\circ$, find the value of $x$.", 
     "options": ["25", "5", "35", "15"], "answer": "25",
     "image_svg": '''<div align="center"><svg width="200" height="120" xmlns="http://www.w3.org/2000/svg"><line x1="20" y1="30" x2="180" y2="30" stroke="#333" stroke-width="2"/><line x1="20" y1="90" x2="180" y2="90" stroke="#333" stroke-width="2"/><line x1="50" y1="110" x2="150" y2="10" stroke="#ff4b4b" stroke-width="2"/></svg></div>''',
     "solution": r"Parallel lines $\rightarrow$ alternate interior angles are equal: $3x - 15 = 2x + 10 \rightarrow x = 25$."},

    {"id": 305, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", "question": r"Evaluate: $\log_2(64) + \log_3(27)$.", "options": ["9", "8", "7", "10"], "answer": "9", "solution": r"$6 + 3 = 9$."},
    {"id": 306, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", "question": r"If $x+1/x=4$, find $x^2+1/x^2$.", "options": ["14", "16", "18", "12"], "answer": "14", "solution": r"$(x+1/x)^2 - 2 = 16 - 2 = 14$."},
    {"id": 307, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", "question": r"Volume of a cone with radius 3 and height 4?", "options": ["$12\pi$", "$36\pi$", "$16\pi$", "$4\pi$"], "answer": "$12\pi$", "solution": r"$1/3\pi(9)(4) = 12\pi$."},
    {"id": 308, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", "question": r"How many ways to arrange the letters in 'MATH'?", "options": ["24", "12", "4", "48"], "answer": "24", "solution": r"$4! = 24$."},
    {"id": 309, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", "question": r"Rationalize: $1 / (\sqrt{3}-\sqrt{2})$.", "options": ["$\sqrt{3}+\sqrt{2}$", "1", "$\sqrt{6}$", "$\sqrt{3}-\sqrt{2}$"], "answer": "$\sqrt{3}+\sqrt{2}$", "solution": r"Multiply by conjugate: $(\sqrt{3}+\sqrt{2})/(3-2)$."},
    {"id": 310, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", "question": r"Vertex of $y = x^2-4x+7$?", "options": ["(2, 3)", "(2, 7)", "(-2, 3)", "(4, 7)"], "answer": "(2, 3)", "solution": r"$x=-b/2a=2, y=4-8+7=3$."},
    {"id": 311, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", "question": r"Area of a hexagon with side 2?", "options": ["$6\sqrt{3}$", "$12\sqrt{3}$", "$3\sqrt{3}$", "6"], "answer": "$6\sqrt{3}$", "solution": r"$3\sqrt{3}/2 \times s^2 = 6\sqrt{3}$."},
    {"id": 312, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", "question": r"Probability of 3 heads in 3 coin flips?", "options": ["1/8", "1/4", "1/2", "1/6"], "answer": "1/8", "solution": r"$(1/2)^3 = 1/8$."},
    {"id": 313, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", "question": r"Find $x$: $2^x \times 4 = 32$.", "options": ["3", "4", "5", "2"], "answer": "3", "solution": r"$2^x \times 2^2 = 2^5 \rightarrow x+2=5 \rightarrow x=3$."},
    {"id": 314, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", "question": r"Sum of roots of $x^2-10x+21=0$?", "options": ["10", "21", "7", "3"], "answer": "10", "solution": r"$-b/a = 10$."},
    {"id": 315, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", "question": r"Distance between (1,1) and (4,5)?", "options": ["5", "7", "4", "25"], "answer": "5", "solution": r"$\sqrt{(4-1)^2 + (5-1)^2} = 5$."},
    {"id": 316, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", "question": r"Number of ways to choose 2 items from 5?", "options": ["10", "20", "5", "25"], "answer": "10", "solution": r"$5C2 = 10$."},
    {"id": 317, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", "question": r"Evaluate: $8^{2/3}$.", "options": ["4", "2", "16", "8"], "answer": "4", "solution": r"$(\sqrt[3]{8})^2 = 2^2 = 4$."},
    {"id": 318, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", "question": r"Find the domain of $1/\sqrt{x-5}$.", "options": ["$x > 5$", "$x \geq 5$", "$x \neq 5$", "All x"], "answer": "$x > 5$", "solution": r"$x-5 > 0$."},
    {"id": 319, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", "question": r"Total interior angles of a decagon?", "options": ["1440°", "1800°", "1260°", "1620°"], "answer": "1440°", "solution": r"$(10-2) \times 180 = 1440$."},
    {"id": 320, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", "question": r"Remainder when $x^2-5x+6$ is divided by $x-1$?", "options": ["2", "0", "6", "1"], "answer": "2", "solution": r"Plug in 1: $1-5+6 = 2$."}
]
