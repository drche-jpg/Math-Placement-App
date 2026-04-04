# questions.py
all_questions = [
    # LEVEL 1: EASY
    {"id": 101, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", 
     "question": r"Compute the exact value of the numerical expression $15 - (-4) + 3 \times (2^2 - 2)$ following the standard order of operations.", 
     "options": ["13", "25", "19", "11"], "answer": "25", 
     "solution": r"$15 + 4 + 3(2) = 19 + 6 = 25$."},
    
    {"id": 102, "difficulty": "Level 1: Easy", "category": "Number Sense & Operations", 
     "question": r"In a laboratory experiment, a liquid starts at $-12^\circ\text{C}$ and rises by $25^\circ\text{C}$. What is the final temperature?", 
     "options": ["-13", "12", "13", "37"], "answer": "13", 
     "solution": r"$-12 + 25 = 13$."},

    {"id": 104, "difficulty": "Level 1: Easy", "category": "Number Theory & Probability", 
     "question": r"Identify the Greatest Common Factor (GCF) of the set $\{48, 72, 120\}$.", 
     "options": ["12", "36", "24", "6"], "answer": "24", 
     "solution": r"The largest integer dividing all three is 24."},

    {"id": 107, "difficulty": "Level 1: Easy", "category": "Geometry & Data", 
     "question": r"A rectangular field has a perimeter of 40m. If the length is 4m longer than the width, calculate the area in m².", 
     "options": ["100", "96", "84", "120"], "answer": "96", 
     "solution": r"Width=8, Length=12. $8 \times 12 = 96$."},

    {"id": 108, "difficulty": "Level 1: Easy", "category": "Geometry & Data", 
     "question": r"Determine the sum of the interior angles of a regular pentagon.", 
     "options": ["360°", "720°", "540°", "180°"], "answer": "540°", 
     "solution": r"$(5-2) \times 180 = 540$."},

    # LEVEL 2: INTERMEDIATE
    {"id": 201, "difficulty": "Level 2: Intermediate", "category": "Number Sense & Operations", 
     "question": r"Evaluate: $\frac{2^5 \times 3^4}{2^3 \times 3^2} - \sqrt{144}$.", 
     "options": ["12", "48", "36", "24"], "answer": "24", 
     "solution": r"$36 - 12 = 24$."},

    {"id": 204, "difficulty": "Level 2: Intermediate", "category": "Geometry & Data", 
     "question": r"A cylindrical tank has radius 3m and height 7m. Using $\pi \approx 22/7$, find the volume.", 
     "options": ["66", "198", "462", "154"], "answer": "198",
     "image_svg": '''<div align="center"><svg width="100" height="100"><ellipse cx="50" cy="20" rx="30" ry="10" stroke="#333" fill="none"/><line x1="20" y1="20" x2="20" y2="80" stroke="#333"/><line x1="80" y1="20" x2="80" y2="80" stroke="#333"/><ellipse cx="50" cy="80" rx="30" ry="10" stroke="#333" fill="none" stroke-dasharray="2,2"/></svg></div>''',
     "solution": r"$\pi r^2 h = (22/7) \times 9 \times 7 = 198$."},

    # LEVEL 3: DIFFICULT
    {"id": 304, "difficulty": "Level 3: Difficult", "category": "Geometry & Data", 
     "question": r"Two parallel lines are intersected by a transversal. If alternate interior angles are $(3x-15)^\circ$ and $(2x+10)^\circ$, find $x$.", 
     "options": ["5", "25", "15", "35"], "answer": "25",
     "image_svg": '''<div align="center"><svg width="200" height="100"><line x1="20" y1="30" x2="180" y2="30" stroke="#333" stroke-width="2"/><line x1="20" y1="70" x2="180" y2="70" stroke="#333" stroke-width="2"/><line x1="50" y1="90" x2="150" y2="10" stroke="#ff4b4b" stroke-width="2"/></svg></div>''',
     "solution": r"$3x-15 = 2x+10 \rightarrow x=25$."},

    {"id": 316, "difficulty": "Level 3: Difficult", "category": "Number Theory & Probability", 
     "question": r"Compute the remainder when $2^{2026}$ is divided by 7.", 
     "options": ["4", "1", "2", "0"], "answer": "2", 
     "solution": r"Cycle is 2, 4, 1. $2026 \equiv 1 \pmod 3$, so remainder is 2."},
    
    # ... [Continue this pattern for all 60 questions]
]
