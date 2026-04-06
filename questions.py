# questions.py

all_questions = [
    # ==========================================
    # LEVEL 1: EASY (Foundational Grade 7-8)
    # ==========================================
    {"id": 101, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", 
     "question": r"Compute the exact value of the numerical expression $15 - (-4) + 3 \times (2^2 - 2)$ by following the standard mathematical order of operations.", 
     "options": ["25", "13", "11", "19"], "answer": "25", 
     "solution": r"Simplify inside the parentheses: $2^2 - 2 = 4 - 2 = 2$. Multiply: $3 \times 2 = 6$. The expression becomes $15 + 4 + 6 = 25$."},
    
    {"id": 102, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", 
     "question": r"In a controlled laboratory experiment, a liquid starts at an initial temperature of $-12^\circ\text{C}$. If the liquid is heated at a constant rate until its temperature rises by exactly $25^\circ\text{C}$, what is the final recorded temperature?", 
     "options": [r"$13^\circ\text{C}$", r"$-13^\circ\text{C}$", r"$37^\circ\text{C}$", r"$12^\circ\text{C}$"], "answer": r"$13^\circ\text{C}$", 
     "solution": r"The final temperature is found by the sum: $-12 + 25 = 13$."},

    {"id": 103, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", 
     "question": r"A bakery uses a specific ratio of 300 grams of flour to produce 4 loaves of bread. Determine the total amount of flour required, in grams, to produce 10 loaves of the same bread.", 
     "options": ["750g", "600g", "900g", "1200g"], "answer": "750g", 
     "solution": r"Flour per loaf: $300 / 4 = 75\text{g}$. For 10 loaves: $75 \times 10 = 750\text{g}$."},

    {"id": 104, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", 
     "question": r"Identify the Greatest Common Factor (GCF) of the set of integers $\{48, 72, 120\}$.", 
     "options": ["24", "12", "6", "36"], "answer": "24", 
     "solution": r"Factors of 48: $2^4 \cdot 3$. Factors of 72: $2^3 \cdot 3^2$. Factors of 120: $2^3 \cdot 3 \cdot 5$. Common factors: $2^3 \cdot 3 = 24$."},

    {"id": 105, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", 
     "question": r"Determine the value of $x$ that satisfies the linear equation $5(x - 2) = 3(x + 4)$.", 
     "options": ["11", "1", "22", "5"], "answer": "11", 
     "solution": r"Expand: $5x - 10 = 3x + 12$. Rearrange: $2x = 22$. Thus, $x = 11$."},

    {"id": 106, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", 
     "question": r"If $a = 4$ and $b = -3$, compute the value of the algebraic expression $a^2 - 2b + 5$.", 
     "options": ["27", "15", "21", "19"], "answer": "27", 
     "solution": r"Substitute values: $4^2 - 2(-3) + 5 = 16 + 6 + 5 = 27$."},

    {"id": 107, "difficulty": "Level 1: Easy", "category": "Geometry & Data", 
     "question": r"A rectangular field has a perimeter of 40 meters. If the length is 4 meters longer than the width, calculate the total area of the field in square meters.", 
     "options": ["96", "84", "100", "120"], "answer": "96", 
     "solution": r"$2(w + w+4) = 40 \rightarrow 4w+8=40 \rightarrow w=8, l=12$. Area $= 12 \times 8 = 96$."},

    {"id": 108, "difficulty": "Level 1: Easy", "category": "Geometry & Data", 
     "question": r"A regular pentagon is inscribed in a circle. Determine the sum of the interior angles of this pentagon.", 
     "options": ["540°", "360°", "720°", "180°"], "answer": "540°", 
     "solution": r"Using $(n-2) \times 180$: $(5-2) \times 180 = 3 \times 180 = 540^\circ$."},

    {"id": 109, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", 
     "question": r"A fair six-sided die is rolled twice. What is the probability that the sum of the two numbers shown is exactly 5?", 
     "options": ["1/9", "1/6", "4/36", "1/12"], "answer": "1/9", 
     "solution": r"Pairs: (1,4), (2,3), (3,2), (4,1). Total outcomes: 36. Prob: $4/36 = 1/9$."},

    {"id": 110, "difficulty": "Level 1: Easy", "category": "Geometry & Data", 
     "question": r"Find the arithmetic mean (average) of the data set $\{14, 22, 18, 30, 16\}$.", 
     "options": ["20", "18", "22", "25"], "answer": "20", 
     "solution": r"Sum = 100. Count = 5. $100 / 5 = 20$."},

    {"id": 111, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", 
     "question": r"Convert the fraction $7/8$ into its equivalent percentage form.", 
     "options": ["87.5%", "78%", "82.5%", "75%"], "answer": "87.5%", 
     "solution": r"$7 \div 8 = 0.875$. Multiplying by 100 yields $87.5\%$."},

    {"id": 112, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", 
     "question": r"The sum of three consecutive integers is 72. What is the value of the largest of these three integers?", 
     "options": ["25", "23", "24", "26"], "answer": "25", 
     "solution": r"$x + (x+1) + (x+2) = 72 \rightarrow 3x+3=72 \rightarrow x=23$. Largest is $23+2=25$."},

    {"id": 113, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", 
     "question": r"Identify the next term in the arithmetic sequence: $3, 7, 11, 15, \dots$", 
     "options": ["19", "17", "21", "23"], "answer": "19", 
     "solution": r"The common difference is $+4$. $15 + 4 = 19$."},

    {"id": 114, "difficulty": "Level 1: Easy", "category": "Geometry & Data", 
     "question": r"A square has a total perimeter of 32 cm. Compute the area of this square in square centimeters.", 
     "options": ["64", "32", "16", "48"], "answer": "64", 
     "solution": r"Side $= 32 / 4 = 8$. Area $= 8^2 = 64$."},

    {"id": 115, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", 
     "question": r"What is the result of dividing $1.2$ by $0.3$ and then adding the product of $0.5$ and $4$?", 
     "options": ["6", "4.2", "2.2", "10"], "answer": "6", 
     "solution": r"$(1.2 / 0.3) + (0.5 \times 4) = 4 + 2 = 6$."},

    {"id": 116, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", 
     "question": r"How many prime numbers exist between the integers 10 and 30?", 
     "options": ["6", "5", "4", "7"], "answer": "6", 
     "solution": r"The primes are: 11, 13, 17, 19, 23, 29. Total = 6."},

    {"id": 117, "difficulty": "Level 1: Easy", "category": "Pre-Algebra & Equations", 
     "question": r"Simplify the algebraic expression by combining like terms: $2(x+3) - 3(x-1)$.", 
     "options": ["-x + 9", "-x + 3", "x + 9", "5x + 3"], "answer": "-x + 9", 
     "solution": r"$2x + 6 - 3x + 3 = -x + 9$."},

    {"id": 118, "difficulty": "Level 1: Easy", "category": "Geometry & Data", 
     "question": r"A cube has a volume of 27 cubic centimeters. Determine the total surface area of the cube in square centimeters.", 
     "options": ["54", "36", "9", "27"], "answer": "54", 
     "solution": r"Side $= \sqrt[3]{27} = 3$. Surface Area $= 6 \times 3^2 = 54$."},

    {"id": 119, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", 
     "question": r"Calculate $0.4\%$ of 500.", 
     "options": ["2", "20", "200", "0.2"], "answer": "2", 
     "solution": r"$0.004 \times 500 = 2$."},

    {"id": 120, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", 
     "question": r"A bag contains 5 red, 3 blue, and 2 green marbles. If one marble is drawn at random, what is the probability that it is NOT blue?", 
     "options": ["7/10", "3/10", "1/2", "4/5"], "answer": "7/10", 
     "solution": r"Total = 10. Blue = 3. Non-blue = $10 - 3 = 7$. Prob = 7/10."},

    # ==========================================
    # LEVEL 2: INTERMEDIATE (Grade 8-9 Standard)
    # ==========================================
    {"id": 201, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", 
     "question": r"Evaluate the expression by applying the laws of exponents and order of operations: $\frac{2^5 \times 3^4}{2^3 \times 3^2} - \sqrt{144}$.", 
     "options": ["24", "36", "12", "48"], "answer": "24", 
     "solution": r"Simplify exponents: $2^2 \times 3^2 = 4 \times 9 = 36$. $\sqrt{144} = 12$. $36 - 12 = 24$."},

    {"id": 202, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", 
     "question": r"Determine the total number of distinct positive factors for the integer 72.", 
     "options": ["12", "10", "8", "16"], "answer": "12", 
     "solution": r"$72 = 2^3 \cdot 3^2$. Factors = $(3+1)(2+1) = 4 \times 3 = 12$."},

    {"id": 203, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", 
     "question": r"A taxi company charges a base fee of $5.00 plus an additional $2.50 per mile traveled. If a passenger's total fare was $35.00, compute the total distance traveled in miles.", 
     "options": ["12", "14", "10", "15"], "answer": "12", 
     "solution": r"$5 + 2.5m = 35 \rightarrow 2.5m = 30 \rightarrow m = 12$."},

    {"id": 204, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", 
     "question": r"A cylindrical water tank has a radius of 3 meters and a height of 7 meters. Using $\pi \approx 22/7$, calculate the total volume of the tank in cubic meters.", 
     "options": ["198", "66", "462", "154"], "answer": "198",
     "image_svg": '''<div align="center"><svg width="100" height="120"><ellipse cx="50" cy="20" rx="30" ry="10" stroke="#333" fill="none"/><line x1="20" y1="20" x2="20" y2="100" stroke="#333"/><line x1="80" y1="20" x2="80" y2="100" stroke="#333"/><ellipse cx="50" cy="100" rx="30" ry="10" stroke="#333" fill="none" stroke-dasharray="2,2"/></svg></div>''',
     "solution": r"Volume $= \pi r^2 h = (22/7) \times 9 \times 7 = 22 \times 9 = 198$."},

    {"id": 205, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", 
     "question": r"Simplify the complex fraction: $\frac{1/2 + 1/3}{1/4}$.", 
     "options": ["10/3", "5/12", "1/6", "2"], "answer": "10/3", 
     "solution": r"Numerator: $3/6 + 2/6 = 5/6$. Result: $5/6 \times 4 = 20/6 = 10/3$."},

    {"id": 206, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", 
     "question": r"Compute the solution set for $x$ in the quadratic equation: $x^2 - 5x + 6 = 0$.", 
     "options": ["2, 3", "-2, -3", "1, 6", "0, 5"], "answer": "2, 3", 
     "solution": r"Factor: $(x-2)(x-3)=0$. Roots are 2 and 3."},

    {"id": 207, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", 
     "question": r"Determine the length of the hypotenuse of a right-angled triangle with leg lengths of 9 units and 12 units.", 
     "options": ["15", "21", "13", "144"], "answer": "15", 
     "solution": r"$\sqrt{9^2 + 12^2} = \sqrt{81 + 144} = \sqrt{225} = 15$."},

    {"id": 208, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", 
     "question": r"In a standard deck of 52 playing cards, what is the probability of randomly drawing either a King or a Queen?", 
     "options": ["2/13", "1/13", "4/13", "1/26"], "answer": "2/13", 
     "solution": r"8 target cards (4 Kings, 4 Queens). $8/52 = 2/13$."},

    {"id": 209, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", 
     "question": r"Represent the decimal value $0.00045$ in proper scientific notation.", 
     "options": ["$4.5 \times 10^{-4}$", "$4.5 \times 10^{-5}$", "$45 \times 10^{-5}$", "0.45"], "answer": "$4.5 \times 10^{-4}$", 
     "solution": r"Move decimal 4 places right: $4.5 \times 10^{-4}$."},

    {"id": 210, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", 
     "question": r"Solve the simultaneous linear system: $x + y = 10$ and $x - y = 2$. Find $(x, y)$.", 
     "options": ["(6, 4)", "(5, 5)", "(7, 3)", "(8, 2)"], "answer": "(6, 4)", 
     "solution": r"Add equations: $2x = 12 \rightarrow x=6$. Substitute: $6+y=10 \rightarrow y=4$."},

    {"id": 211, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", 
     "question": r"Compute the interior angle measure, in degrees, of a regular hexagon.", 
     "options": ["120°", "108°", "90°", "135°"], "answer": "120°", 
     "solution": r"Sum $= (6-2) \times 180 = 720$. Angle $= 720 / 6 = 120^\circ$."},

    {"id": 212, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", 
     "question": r"Determine the units digit of the large power $3^{40}$.", 
     "options": ["1", "3", "9", "7"], "answer": "1", 
     "solution": r"Cycle of 3: 3, 9, 7, 1 (length 4). $40 \div 4 = 10$ remainder 0. Units digit is 1."},

    {"id": 213, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", 
     "question": r"Compute the value of $2.5^2 - 1.5^2$.", 
     "options": ["4", "5", "6.25", "1"], "answer": "4", 
     "solution": r"$(2.5-1.5)(2.5+1.5) = 1 \times 4 = 4$."},

    {"id": 214, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", 
     "question": r"Let $f(x) = 3x - 5$. Compute the composite value $f(f(2))$.", 
     "options": ["-2", "1", "2", "-5"], "answer": "-2", 
     "solution": r"$f(2) = 3(2)-5 = 1$. $f(1) = 3(1)-5 = -2$."},

    {"id": 215, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", 
     "question": r"Calculate the exact area of an equilateral triangle with a side length of 4 units.", 
     "options": ["$4\sqrt{3}$", "8", "$8\sqrt{3}$", "4"], "answer": "$4\sqrt{3}$", 
     "solution": r"Area $= s^2\sqrt{3}/4 = 16\sqrt{3}/4 = 4\sqrt{3}$."},

    {"id": 216, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", 
     "question": r"How many integers between 1 and 100 are divisible by both 3 and 5?", 
     "options": ["6", "5", "7", "10"], "answer": "6", 
     "solution": r"Must be divisible by LCM(3,5)=15. Multiples: 15, 30, 45, 60, 75, 90. Total = 6."},

    {"id": 217, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", 
     "question": r"Simplify the radical expression $\sqrt{72} \div \sqrt{2}$.", 
     "options": ["6", "36", "12", "18"], "answer": "6", 
     "solution": r"$\sqrt{72/2} = \sqrt{36} = 6$."},

    {"id": 218, "difficulty": "Level 2: Intermediate", "category": "Pre-Algebra & Equations", 
     "question": r"Determine the slope of the line represented by the equation $2x + 3y = 6$.", 
     "options": ["-2/3", "2/3", "-2", "2"], "answer": "-2/3", 
     "solution": r"$3y = -2x + 6 \rightarrow y = -2/3x + 2$. Slope $= -2/3$."},

    {"id": 219, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", 
     "question": r"Find the volume of a sphere with a radius of 3 units in terms of $\pi$.", 
     "options": ["$36\pi$", "$12\pi$", "$9\pi$", "$27\pi$"], "answer": "$36\pi$", 
     "solution": r"Volume $= 4/3 \pi r^3 = 4/3 \pi (27) = 36\pi$."},

    {"id": 220, "difficulty": "Level 2: Intermediate", "category": "Number Theory & Probability", 
     "question": r"Compute the sum of the interior angles of a convex octagon.", 
     "options": ["1080°", "720°", "900°", "1440°"], "answer": "1080°", 
     "solution": r"$(8-2) \times 180 = 6 \times 180 = 1080^\circ$."},

    # ==========================================
    # LEVEL 3: DIFFICULT (Advanced/Olympiad)
    # ==========================================
    {"id": 301, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", 
     "question": r"Consider the infinite nested radical $x = \sqrt{6 + \sqrt{6 + \sqrt{6 + \dots}}}$. Determine the positive integer value of $x$.", 
     "options": ["3", "2", "6", "9"], "answer": "3", 
     "solution": r"$x = \sqrt{6+x} \rightarrow x^2 - x - 6 = 0 \rightarrow (x-3)(x+2)=0$. $x=3$."},

    {"id": 302, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", 
     "question": r"Compute the remainder when the large power $2^{2026}$ is divided by 7.", 
     "options": ["2", "4", "1", "0"], "answer": "2", 
     "solution": r"Cycle of $2^n \pmod 7$: 2, 4, 1. $2026 \div 3$ rem 1. Same as $2^1 = 2$."},

    {"id": 303, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", 
     "question": r"In a group of 30 students, 18 play soccer, 15 play basketball, and 5 play neither sport. How many students play both soccer and basketball?", 
     "options": ["8", "10", "5", "12"], "answer": "8", 
     "solution": r"Total playing = $30-5=25$. Both = $(18+15)-25 = 8$."},

    {"id": 304, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", 
     "question": r"Two parallel lines are intersected by a transversal. If alternate interior angles measure $(3x - 15)^\circ$ and $(2x + 10)^\circ$, find the value of $x$.", 
     "options": ["25", "5", "35", "15"], "answer": "25",
     "image_svg": '''<div align="center"><svg width="200" height="120"><line x1="20" y1="30" x2="180" y2="30" stroke="#333" stroke-width="2"/><line x1="20" y1="90" x2="180" y2="90" stroke="#333" stroke-width="2"/><line x1="50" y1="110" x2="150" y2="10" stroke="#ff4b4b" stroke-width="2"/></svg></div>''',
     "solution": r"Parallel lines $\rightarrow$ alternate interior angles are equal: $3x - 15 = 2x + 10 \rightarrow x = 25$."},

    {"id": 305, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", 
     "question": r"Determine the exact value of the sum $\sqrt{75} + \sqrt{48} - \sqrt{27}$.", 
     "options": [r"$6\sqrt{3}$", r"$12\sqrt{3}$", r"$8\sqrt{3}$", r"$\sqrt{96}$"], "answer": r"$6\sqrt{3}$", 
     "solution": r"$5\sqrt{3} + 4\sqrt{3} - 3\sqrt{3} = 6\sqrt{3}$."},

    {"id": 306, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", 
     "question": r"If $x + 1/x = 4$, determine the value of $x^2 + 1/x^2$.", 
     "options": ["14", "16", "18", "12"], "answer": "14", 
     "solution": r"$(x+1/x)^2 = x^2 + 2 + 1/x^2 = 16 \rightarrow x^2 + 1/x^2 = 14$."},

    {"id": 307, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", 
     "question": r"Calculate the volume of a right circular cone with a radius of 3 units and a height of 4 units.", 
     "options": ["$12\pi$", "$36\pi$", "$16\pi$", "$4\pi$"], "answer": "$12\pi$", 
     "solution": r"Volume $= 1/3 \pi r^2 h = 1/3 \pi (9)(4) = 12\pi$."},

    {"id": 308, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", 
     "question": r"Determine the number of unique permutations of the letters in the word 'MATH'.", 
     "options": ["24", "12", "4", "48"], "answer": "24", 
     "solution": r"$4! = 4 \times 3 \times 2 \times 1 = 24$."},

    {"id": 309, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", 
     "question": r"Rationalize the denominator of the expression $1 / (\sqrt{3}-\sqrt{2})$.", 
     "options": [r"$\sqrt{3}+\sqrt{2}$", "1", r"$\sqrt{6}$", r"$\sqrt{3}-\sqrt{2}$"], "answer": r"$\sqrt{3}+\sqrt{2}$", 
     "solution": r"Multiply top and bottom by conjugate $(\sqrt{3}+\sqrt{2})$. Denom becomes $3-2=1$."},

    {"id": 310, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", 
     "question": r"Identify the vertex of the parabola defined by the equation $y = x^2 - 4x + 7$.", 
     "options": ["(2, 3)", "(2, 7)", "(-2, 3)", "(4, 7)"], "answer": "(2, 3)", 
     "solution": r"$x = -b/2a = 4/2 = 2$. $y = 4 - 8 + 7 = 3$."},

    {"id": 311, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", 
     "question": r"Compute the exact area of a regular hexagon with a side length of 2 units.", 
     "options": ["$6\sqrt{3}$", "$12\sqrt{3}$", "$3\sqrt{3}$", "6"], "answer": ["$6\sqrt{3}$"], "answer": "$6\sqrt{3}$", 
     "solution": r"Area $= 3\sqrt{3}/2 \times s^2 = 3\sqrt{3}/2 \times 4 = 6\sqrt{3}$."},

    {"id": 312, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", 
     "question": r"A fair coin is tossed three times. What is the probability of getting exactly three heads?", 
     "options": ["1/8", "1/4", "1/2", "1/6"], "answer": "1/8", 
     "solution": r"$(1/2)^3 = 1/8$."},

    {"id": 313, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", 
     "question": r"Solve for $x$ in the exponential equation $2^x \times 4 = 32$.", 
     "options": ["3", "4", "5", "2"], "answer": "3", 
     "solution": r"$2^x \cdot 2^2 = 2^5 \rightarrow x+2=5 \rightarrow x=3$."},

    {"id": 314, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", 
     "question": r"Determine the sum of the roots of the quadratic equation $x^2 - 10x + 21 = 0$.", 
     "options": ["10", "21", "7", "3"], "answer": "10", 
     "solution": r"Sum of roots $= -b/a = 10$."},

    {"id": 315, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", 
     "question": r"Compute the distance between the points $(1,1)$ and $(4,5)$ on the Cartesian plane.", 
     "options": ["5", "7", "4", "25"], "answer": "5", 
     "solution": r"$\sqrt{(4-1)^2 + (5-1)^2} = \sqrt{9+16} = 5$."},

    {"id": 316, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", 
     "question": r"Determine the number of ways to choose a committee of 2 members from a group of 5 students.", 
     "options": ["10", "20", "5", "25"], "answer": "10", 
     "solution": r"$5C2 = 10$."},

    {"id": 317, "difficulty": "Level 3: Difficult", "category": "Number Sense & Operations", 
     "question": r"Evaluate the radical exponent: $8^{2/3}$.", 
     "options": ["4", "2", "16", "8"], "answer": "4", 
     "solution": r"$\sqrt[3]{8}^2 = 2^2 = 4$."},

    {"id": 318, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", 
     "question": r"Determine the domain of the real-valued function $f(x) = \frac{1}{\sqrt{x-5}}$.", 
     "options": ["$x > 5$", "$x \geq 5$", "$x \neq 5$", "All x"], "answer": "$x > 5$", 
     "solution": r"Radicand must be positive: $x-5 > 0 \rightarrow x > 5$."},

    {"id": 319, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", 
     "question": r"Calculate the sum of the interior angles of a convex decagon.", 
     "options": ["1440°", "1800°", "1260°", "1620°"], "answer": "1440°", 
     "solution": r"$(10-2) \times 180 = 1440^\circ$."},
  
       {"id": 321, "difficulty": "Level 3: Difficult", "category": "Pre-Algebra & Equations", 
     "question": r"Let $f(x) = (2x^2 + 7x + 3)(x^2 - 2x - 15)$. The graph of $f(x)$ in the coordinate plane is translated 4 units to the right and then rotated about the origin by 180 degrees. The resulting graph is the graph of the function $g(x)$. Compute the sum of the distinct roots of $g(x)$.", 
     "options": ["-1", "-23/2", "-5", "-27/2"], "answer": "-27/2", 
     "solution": r"Let the original function be $f(x) = (2x^2 + 7x + 3)(x^2 - 2x - 15)$.

First, we find the roots of $f(x)$ by setting $f(x) = 0$.

We factor each quadratic expression:
1. $2x^2 + 7x + 3 = 0$
   $(2x + 1)(x + 3) = 0$
   The roots are $x = -\frac{1}{2}$ and $x = -3$.
2. $x^2 - 2x - 15 = 0$
   $(x - 5)(x + 3) = 0$
   The roots are $x = 5$ and $x = -3$.

The distinct roots of $f(x)$ are $r_1 = -\frac{1}{2}$, $r_2 = -3$, and $r_3 = 5$.

Next, we analyze the transformations to find $g(x)$.
Starting with $y = f(x)$:
1. Translated 4 units to the right: This transformation replaces $x$ with $(x - 4)$. So, the new function is $y_1 = f(x - 4)$.
2. Rotated about the origin by 180 degrees: A rotation of 180 degrees about the origin maps a point $(X, Y)$ to $(-X, -Y)$.
   If $(X, Y)$ is a point on $y_1 = f(X - 4)$, then $Y = f(X - 4)$.
   Let the new coordinates be $(x_{new}, y_{new})$. So $x_{new} = -X$ and $y_{new} = -Y$.
   This implies $X = -x_{new}$ and $Y = -y_{new}$.
   Substituting these into $Y = f(X - 4)$:
   $-y_{new} = f(-x_{new} - 4)$
   $y_{new} = -f(-x_{new} - 4)$
   So, the function $g(x)$ is $g(x) = -f(-x - 4)$.

We need to compute the sum of the distinct roots of $g(x)$, which means we need to solve $g(x) = 0$.
$-f(-x - 4) = 0$
$f(-x - 4) = 0$

This means that the expression $(-x - 4)$ must be equal to one of the distinct roots of $f(x)$.

Case 1: $-x - 4 = -\frac{1}{2}$
   $-x = 4 - \frac{1}{2}$
   $-x = \frac{8}{2} - \frac{1}{2}$
   $-x = \frac{7}{2}$
   $x = -\frac{7}{2}$

Case 2: $-x - 4 = -3$
   $-x = 4 - 3$
   $-x = 1$
   $x = -1$

Case 3: $-x - 4 = 5$
   $-x = 4 + 5$
   $-x = 9$
   $x = -9$

The distinct roots of $g(x)$ are $- \frac{7}{2}$, $-1$, and $-9$.

Finally, we compute the sum of these distinct roots:
Sum $= -\frac{7}{2} + (-1) + (-9)$
Sum $= -\frac{7}{2} - 10$
Sum $= -\frac{7}{2} - \frac{20}{2}$
Sum $= -\frac{27}{2}$"},
]
