"""
Comprehensive Mathematics Dataset Generator
Covers: Basic Arithmetic → Class 10 CBSE/NCERT Mathematics
Includes: All formulas, tricks, definitions, examples in Q&A format.
"""
import random

data = []

def add(q, a, reps=5):
    for _ in range(reps):
        data.append(f"Instruction: {q}\nResponse: {a}\n")

# ══════════════════════════════════════════════════════
# 1. NUMBER SYSTEM
# ══════════════════════════════════════════════════════
add("what are natural numbers", "Natural numbers are counting numbers starting from 1. N = {1, 2, 3, 4, 5, ...}. They do not include 0 or negative numbers.")
add("what are whole numbers", "Whole numbers include all natural numbers plus zero. W = {0, 1, 2, 3, 4, ...}.")
add("what are integers", "Integers include all whole numbers and their negatives. Z = {..., -3, -2, -1, 0, 1, 2, 3, ...}.")
add("what are rational numbers", "Rational numbers are numbers that can be written as p/q where p and q are integers and q ≠ 0. Examples: 1/2, -3/4, 5, 0.75.")
add("what are irrational numbers", "Irrational numbers cannot be written as p/q. Their decimal expansions are non-terminating and non-repeating. Examples: √2, √3, π.")
add("what are real numbers", "Real numbers include all rational and irrational numbers. Every point on the number line represents a real number.")
add("what is the difference between rational and irrational numbers", "Rational numbers can be expressed as p/q (fraction of two integers). Irrational numbers cannot — their decimals never end and never repeat. Example: 1/3 = 0.333... (rational), √2 = 1.41421... (irrational).")
add("is √2 rational or irrational", "√2 is irrational. Its decimal expansion is 1.41421356... which is non-terminating and non-repeating. It cannot be expressed as p/q.")
add("is π rational or irrational", "π (pi) is irrational. Its value is approximately 3.14159265... and it cannot be expressed as an exact fraction.")
add("what is a prime number", "A prime number has exactly two factors: 1 and itself. Examples: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29. Note: 2 is the only even prime number.")
add("what is a composite number", "A composite number has more than two factors. Examples: 4, 6, 8, 9, 10, 12. Note: 1 is neither prime nor composite.")
add("what is 1 — prime or composite", "1 is neither prime nor composite. It has only one factor (itself), so it does not qualify as prime or composite.")
add("list all prime numbers up to 100", "Prime numbers up to 100: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97. There are 25 prime numbers up to 100.")
add("what are co-prime numbers", "Two numbers are co-prime (relatively prime) if their HCF (GCD) is 1. Examples: 8 and 9 are co-prime because HCF(8,9) = 1.")
add("what is euclid's division lemma", "Euclid's Division Lemma: For any two positive integers a and b, there exist unique integers q and r such that: a = bq + r, where 0 ≤ r < b. Here a is dividend, b is divisor, q is quotient, r is remainder.")
add("what is the fundamental theorem of arithmetic", "Every composite number can be expressed as a product of primes in a unique way (ignoring order). This is called prime factorisation. Example: 12 = 2 × 2 × 3 = 2² × 3.")

# Divisibility Rules
add("what is the divisibility rule for 2", "A number is divisible by 2 if its last digit is 0, 2, 4, 6, or 8 (even). Example: 346 is divisible by 2 because it ends in 6.")
add("what is the divisibility rule for 3", "A number is divisible by 3 if the sum of its digits is divisible by 3. Example: 123 → 1+2+3 = 6, which is divisible by 3, so 123 is divisible by 3.")
add("what is the divisibility rule for 4", "A number is divisible by 4 if its last two digits form a number divisible by 4. Example: 1324 → last two digits are 24, and 24 ÷ 4 = 6, so 1324 is divisible by 4.")
add("what is the divisibility rule for 5", "A number is divisible by 5 if its last digit is 0 or 5. Example: 145, 230 are divisible by 5.")
add("what is the divisibility rule for 6", "A number is divisible by 6 if it is divisible by both 2 and 3. Example: 132 is even (÷2) and 1+3+2=6 (÷3), so it is divisible by 6.")
add("what is the divisibility rule for 7", "To check divisibility by 7: double the last digit, subtract from the remaining number, and check if the result is divisible by 7. Repeat if needed. Example: 343 → 34 - (2×3) = 34 - 6 = 28. 28 ÷ 7 = 4. So 343 is divisible by 7.")
add("what is the divisibility rule for 8", "A number is divisible by 8 if its last three digits form a number divisible by 8. Example: 3120 → last three digits 120 ÷ 8 = 15, so 3120 is divisible by 8.")
add("what is the divisibility rule for 9", "A number is divisible by 9 if the sum of its digits is divisible by 9. Example: 729 → 7+2+9 = 18, and 18 ÷ 9 = 2, so 729 is divisible by 9.")
add("what is the divisibility rule for 10", "A number is divisible by 10 if its last digit is 0. Example: 450, 1000 are divisible by 10.")
add("what is the divisibility rule for 11", "A number is divisible by 11 if the difference between the sum of digits at odd places and sum of digits at even places is 0 or divisible by 11. Example: 1331 → (1+3) - (3+1) = 4-4 = 0. So 1331 is divisible by 11.")

# ══════════════════════════════════════════════════════
# 2. HCF AND LCM
# ══════════════════════════════════════════════════════
add("what is HCF", "HCF (Highest Common Factor), also called GCD (Greatest Common Divisor), is the largest number that divides two or more numbers exactly. Example: HCF(12, 18) = 6.")
add("what is LCM", "LCM (Least Common Multiple) is the smallest number that is a multiple of two or more numbers. Example: LCM(4, 6) = 12.")
add("what is the relationship between HCF and LCM", "For two numbers a and b: HCF × LCM = a × b. Example: HCF(4,6)=2, LCM(4,6)=12. Check: 2 × 12 = 4 × 6 = 24. ✓")
add("how to find HCF by prime factorisation", "Step 1: Find the prime factorisation of each number. Step 2: HCF = product of common prime factors with lowest powers. Example: 12 = 2²×3, 18 = 2×3². HCF = 2¹×3¹ = 6.")
add("how to find LCM by prime factorisation", "Step 1: Find the prime factorisation of each number. Step 2: LCM = product of all prime factors with highest powers. Example: 12 = 2²×3, 18 = 2×3². LCM = 2²×3² = 4×9 = 36.")
add("how to find HCF using Euclid's division", "Euclid's Algorithm: Divide the larger number by the smaller, then replace the larger with the smaller and the smaller with the remainder. Repeat until remainder is 0. The last non-zero divisor is the HCF. Example: HCF(48,18): 48=18×2+12, 18=12×1+6, 12=6×2+0. HCF = 6.")

# ══════════════════════════════════════════════════════
# 3. ARITHMETIC OPERATIONS & BODMAS
# ══════════════════════════════════════════════════════
add("what is BODMAS", "BODMAS is the order of operations: Brackets, Orders (powers/roots), Division, Multiplication, Addition, Subtraction. Always solve in this order. Example: 2 + 3 × 4 = 2 + 12 = 14 (not 20).")
add("what is PEMDAS", "PEMDAS is another name for order of operations: Parentheses, Exponents, Multiplication, Division, Addition, Subtraction. It is the same as BODMAS.")

# Basic arithmetic formulas
for a_val in range(1, 11):
    for b_val in range(1, 11):
        data.append(f"Instruction: what is {a_val} times {b_val}\nResponse: {a_val} × {b_val} = {a_val*b_val}.\n")
        data.append(f"Instruction: {a_val} multiplied by {b_val}\nResponse: {a_val} × {b_val} = {a_val*b_val}.\n")

# Multiplication tricks
add("trick to multiply by 11", "Trick to multiply any 2-digit number by 11: Add the two digits and place the sum in the middle. Example: 23 × 11 → 2(2+3)3 = 253. If the middle sum > 9, carry over. Example: 57 × 11 → 5(5+7)7 → 5(12)7 → 627.")
add("trick to multiply by 9", "Trick to multiply 1–10 by 9: The tens digit is (n-1) and the units digit is (9 minus tens digit). Example: 7×9 → tens = 6, units = 9-6 = 3 → 63. Or use: n×9 = n×10 - n.")
add("trick to multiply by 5", "To multiply any number by 5: Multiply by 10 and divide by 2. Example: 68 × 5 = 680 ÷ 2 = 340.")
add("trick to multiply by 25", "To multiply any number by 25: Multiply by 100 and divide by 4. Example: 36 × 25 = 3600 ÷ 4 = 900.")
add("trick to square a number ending in 5", "To square a number ending in 5: Multiply the tens digit by (tens digit + 1), then append 25. Example: 35² → 3×4=12, append 25 → 1225. Example: 75² → 7×8=56, append 25 → 5625.")
add("trick to find square of numbers near 100", "For numbers near 100: (100+a)² = 10000 + 200a + a². Example: 103² = 10000 + 600 + 9 = 10609. (100-a)² = 10000 - 200a + a². Example: 97² = 10000 - 600 + 9 = 9409.")

# ══════════════════════════════════════════════════════
# 4. FRACTIONS AND DECIMALS
# ══════════════════════════════════════════════════════
add("what is a fraction", "A fraction represents a part of a whole. It is written as p/q where p is the numerator (top) and q is the denominator (bottom). Example: 3/4 means 3 parts out of 4.")
add("what is a proper fraction", "A proper fraction has numerator less than denominator. Example: 2/5, 3/7. Its value is less than 1.")
add("what is an improper fraction", "An improper fraction has numerator greater than or equal to denominator. Example: 7/4, 9/3. Its value is ≥ 1.")
add("what is a mixed fraction", "A mixed fraction combines a whole number and a proper fraction. Example: 2¾ means 2 + 3/4 = 11/4.")
add("how to add fractions", "To add fractions: Make denominators equal (find LCM), then add numerators. Example: 1/3 + 1/4 = 4/12 + 3/12 = 7/12.")
add("how to multiply fractions", "To multiply fractions: Multiply numerators together and denominators together. Example: 2/3 × 3/4 = (2×3)/(3×4) = 6/12 = 1/2.")
add("how to divide fractions", "To divide fractions: Multiply the first fraction by the reciprocal of the second. Example: 2/3 ÷ 4/5 = 2/3 × 5/4 = 10/12 = 5/6.")
add("what is a terminating decimal", "A terminating decimal has a finite number of digits after the decimal point. Example: 1/4 = 0.25, 3/8 = 0.375. A fraction p/q gives a terminating decimal if q has only factors of 2 and 5.")
add("what is a recurring decimal", "A recurring (repeating) decimal has one or more digits that repeat infinitely. Example: 1/3 = 0.333..., 1/7 = 0.142857142857...")

# ══════════════════════════════════════════════════════
# 5. PERCENTAGES
# ══════════════════════════════════════════════════════
add("what is a percentage", "A percentage is a number expressed as a fraction of 100. The symbol % means 'per hundred'. Example: 45% = 45/100 = 0.45.")
add("how to convert fraction to percentage", "To convert fraction to percentage: Multiply by 100. Example: 3/4 = (3/4) × 100 = 75%.")
add("how to convert percentage to fraction", "To convert percentage to fraction: Divide by 100 and simplify. Example: 60% = 60/100 = 3/5.")
add("how to find percentage of a number", "Formula: Percentage of a number = (Percentage/100) × Number. Example: 30% of 150 = (30/100) × 150 = 45.")
add("what is profit and loss", "Profit = Selling Price - Cost Price (when SP > CP). Loss = Cost Price - Selling Price (when CP > SP).")
add("what is profit percentage formula", "Profit% = (Profit / Cost Price) × 100. Example: CP = 200, SP = 250. Profit = 50. Profit% = (50/200) × 100 = 25%.")
add("what is loss percentage formula", "Loss% = (Loss / Cost Price) × 100. Example: CP = 500, SP = 400. Loss = 100. Loss% = (100/500) × 100 = 20%.")
add("formula for selling price when profit percent is given", "SP = CP × (100 + Profit%) / 100. Example: CP = 400, Profit% = 25%. SP = 400 × 125/100 = 500.")
add("formula for selling price when loss percent is given", "SP = CP × (100 - Loss%) / 100. Example: CP = 600, Loss% = 10%. SP = 600 × 90/100 = 540.")
add("what is discount", "Discount = Marked Price - Selling Price. Discount% = (Discount / Marked Price) × 100. SP = MP × (100 - Discount%) / 100.")
add("what is simple interest", "Simple Interest (SI) = (Principal × Rate × Time) / 100. Where P = principal, R = rate per annum, T = time in years.")
add("what is compound interest", "Compound Interest formula: A = P(1 + R/100)ⁿ. CI = A - P. Where A = Amount, P = Principal, R = Rate%, n = number of years.")
add("difference between simple and compound interest", "In Simple Interest, interest is calculated only on principal. In Compound Interest, interest is added to principal each period, so next interest is on a larger amount. CI > SI for same P, R, T (when T > 1 year).")
add("formula for amount in simple interest", "Amount (A) = Principal + SI = P + (PRT/100) = P(1 + RT/100).")

# ══════════════════════════════════════════════════════
# 6. RATIO AND PROPORTION
# ══════════════════════════════════════════════════════
add("what is ratio", "A ratio compares two quantities of the same kind. Ratio of a to b is written as a:b or a/b. Example: If class has 20 boys and 15 girls, ratio = 20:15 = 4:3.")
add("what is proportion", "Proportion states that two ratios are equal. a:b = c:d is written as a:b::c:d. This means a×d = b×c (cross multiplication rule).")
add("what is direct proportion", "Two quantities are in direct proportion if when one increases, the other increases by the same ratio. Formula: x₁/y₁ = x₂/y₂. Example: Speed and distance (at constant time).")
add("what is inverse proportion", "Two quantities are in inverse proportion if when one increases, the other decreases. Formula: x₁×y₁ = x₂×y₂. Example: Workers and time to complete a job.")
add("what is unitary method", "Unitary method finds the value of one unit first, then multiplies. Example: If 5 pens cost ₹35, cost of 1 pen = 35/5 = ₹7. Cost of 8 pens = 7×8 = ₹56.")

# ══════════════════════════════════════════════════════
# 7. EXPONENTS AND POWERS
# ══════════════════════════════════════════════════════
add("what are the laws of exponents", """Laws of Exponents (for base a, exponents m and n):
1. aᵐ × aⁿ = aᵐ⁺ⁿ (same base, add powers)
2. aᵐ ÷ aⁿ = aᵐ⁻ⁿ (same base, subtract powers)
3. (aᵐ)ⁿ = aᵐⁿ (power of power, multiply)
4. (ab)ᵐ = aᵐ × bᵐ (power of product)
5. (a/b)ᵐ = aᵐ / bᵐ (power of quotient)
6. a⁰ = 1 (any non-zero base to power 0 is 1)
7. a⁻ᵐ = 1/aᵐ (negative exponent means reciprocal)""")
add("what is a to the power 0", "Any non-zero number raised to the power 0 equals 1. a⁰ = 1 (where a ≠ 0). Example: 5⁰ = 1, 100⁰ = 1, (3/4)⁰ = 1.")
add("what is a negative exponent", "A negative exponent means take the reciprocal. a⁻ⁿ = 1/aⁿ. Example: 2⁻³ = 1/2³ = 1/8.")
add("what is a fractional exponent", "A fractional exponent represents a root. a^(1/n) = ⁿ√a (nth root of a). Example: 8^(1/3) = ∛8 = 2. 25^(1/2) = √25 = 5.")
add("what are perfect squares up to 20", "Perfect squares up to 20: 1²=1, 2²=4, 3²=9, 4²=16, 5²=25, 6²=36, 7²=49, 8²=64, 9²=81, 10²=100, 11²=121, 12²=144, 13²=169, 14²=196, 15²=225, 16²=256, 17²=289, 18²=324, 19²=361, 20²=400.")
add("what are perfect cubes up to 10", "Perfect cubes up to 10: 1³=1, 2³=8, 3³=27, 4³=64, 5³=125, 6³=216, 7³=343, 8³=512, 9³=729, 10³=1000.")

# ══════════════════════════════════════════════════════
# 8. ALGEBRA BASICS
# ══════════════════════════════════════════════════════
add("what is a variable", "A variable is a symbol (usually a letter like x, y, z) that represents an unknown or changing quantity.")
add("what is a constant", "A constant is a fixed value that does not change. Example: In 3x + 7, the number 7 is a constant.")
add("what is a coefficient", "A coefficient is the number multiplied by a variable. Example: In 5x, the coefficient is 5. In -3y², the coefficient is -3.")
add("what is an algebraic expression", "An algebraic expression combines variables, constants, and operations. Example: 3x + 2y - 5. It has no equals sign.")
add("what is a polynomial", "A polynomial is an algebraic expression with one or more terms, each being a product of a constant and non-negative integer powers of variables. Example: 3x² + 2x - 1.")
add("what is the degree of a polynomial", "The degree of a polynomial is the highest power of the variable. Example: 4x³ + 3x² - x + 2 has degree 3. A linear polynomial has degree 1, quadratic has degree 2, cubic has degree 3.")
add("what is a monomial binomial trinomial", "Monomial: 1 term (e.g., 5x). Binomial: 2 terms (e.g., x + 3). Trinomial: 3 terms (e.g., x² + x + 1). Polynomial: any number of terms.")
add("what are like terms", "Like terms have the same variable(s) raised to the same power(s). Example: 3x and -7x are like terms. 2x² and 5x are NOT like terms (different powers).")
add("how to add polynomials", "To add polynomials: Combine like terms. Example: (3x² + 2x + 1) + (x² - 3x + 5) = (3+1)x² + (2-3)x + (1+5) = 4x² - x + 6.")

# Algebraic Identities
add("what are the standard algebraic identities", """Standard Algebraic Identities:
1. (a + b)² = a² + 2ab + b²
2. (a - b)² = a² - 2ab + b²
3. (a + b)(a - b) = a² - b²
4. (a + b + c)² = a² + b² + c² + 2ab + 2bc + 2ca
5. (a + b)³ = a³ + 3a²b + 3ab² + b³
6. (a - b)³ = a³ - 3a²b + 3ab² - b³
7. a³ + b³ = (a + b)(a² - ab + b²)
8. a³ - b³ = (a - b)(a² + ab + b²)
9. a³ + b³ + c³ - 3abc = (a+b+c)(a²+b²+c²-ab-bc-ca)""")
add("expand (a+b)^2", "(a + b)² = a² + 2ab + b². This is derived by multiplying (a+b)(a+b). Example: (x+3)² = x² + 6x + 9.")
add("expand (a-b)^2", "(a - b)² = a² - 2ab + b². Example: (2x-5)² = 4x² - 20x + 25.")
add("expand (a+b)(a-b)", "(a + b)(a - b) = a² - b². This is the difference of squares identity. Example: (x+4)(x-4) = x² - 16.")
add("expand (a+b)^3", "(a + b)³ = a³ + 3a²b + 3ab² + b³. Example: (x+2)³ = x³ + 6x² + 12x + 8.")
add("expand (a-b)^3", "(a - b)³ = a³ - 3a²b + 3ab² - b³. Example: (x-1)³ = x³ - 3x² + 3x - 1.")
add("what is a3+b3 formula", "a³ + b³ = (a + b)(a² - ab + b²). This is the sum of cubes formula.")
add("what is a3-b3 formula", "a³ - b³ = (a - b)(a² + ab + b²). This is the difference of cubes formula.")

# Factorisation
add("what is factorisation", "Factorisation means expressing a polynomial as a product of simpler polynomials (its factors). Example: x² - 5x + 6 = (x-2)(x-3).")
add("how to factorise by common factor", "Find the common factor of all terms and take it outside. Example: 6x² + 4x = 2x(3x + 2).")
add("how to factorise a quadratic equation", """To factorise ax² + bx + c:
1. Find two numbers p and q such that p × q = a×c and p + q = b.
2. Rewrite bx as px + qx and factor by grouping.
Example: x² + 5x + 6: p×q=6, p+q=5 → p=2, q=3.
x² + 2x + 3x + 6 = x(x+2) + 3(x+2) = (x+2)(x+3).""")

# ══════════════════════════════════════════════════════
# 9. LINEAR EQUATIONS
# ══════════════════════════════════════════════════════
add("what is a linear equation", "A linear equation in one variable is of the form ax + b = 0 (a ≠ 0). Its solution is x = -b/a. It has exactly one solution. Example: 2x + 6 = 0 → x = -3.")
add("what is a linear equation in two variables", "A linear equation in two variables: ax + by + c = 0. It represents a straight line on a graph. Example: 2x + 3y = 12.")
add("how to solve a linear equation", "To solve a linear equation: perform same operations on both sides to isolate the variable. Example: 3x - 7 = 11 → 3x = 18 → x = 6.")
add("methods to solve pair of linear equations", """Methods to solve simultaneous linear equations (pair):
1. Substitution Method: Express one variable in terms of other, substitute.
2. Elimination Method: Multiply equations to make coefficients of one variable equal, then add/subtract.
3. Cross Multiplication Method: a₁x+b₁y+c₁=0 and a₂x+b₂y+c₂=0 → x/(b₁c₂-b₂c₁) = y/(c₁a₂-c₂a₁) = 1/(a₁b₂-a₂b₁).
4. Graphical Method: Plot both lines; intersection point is the solution.""")
add("what is the substitution method", "Substitution Method: From one equation, express one variable in terms of the other. Substitute into the second equation to find the value. Then substitute back. Example: x+y=5 and x-y=1. From eq1: x=5-y. Substitute: (5-y)-y=1 → 5-2y=1 → y=2. Then x=3.")
add("what is the elimination method", "Elimination Method: Multiply equations by suitable numbers to make coefficients of one variable equal, then add or subtract to eliminate that variable. Example: 2x+3y=8 and 3x-3y=7. Add: 5x=15 → x=3. Substitute: 6+3y=8 → y=2/3.")
add("conditions for pair of linear equations", """For a₁x+b₁y+c₁=0 and a₂x+b₂y+c₂=0:
• If a₁/a₂ ≠ b₁/b₂ → Unique solution (lines intersect) — Consistent.
• If a₁/a₂ = b₁/b₂ = c₁/c₂ → Infinitely many solutions (same line) — Consistent (Dependent).
• If a₁/a₂ = b₁/b₂ ≠ c₁/c₂ → No solution (parallel lines) — Inconsistent.""")

# ══════════════════════════════════════════════════════
# 10. QUADRATIC EQUATIONS
# ══════════════════════════════════════════════════════
add("what is a quadratic equation", "A quadratic equation is of the form ax² + bx + c = 0, where a ≠ 0. It has degree 2 and at most two solutions (roots). Example: x² - 5x + 6 = 0.")
add("what is the quadratic formula", "Quadratic Formula: x = [-b ± √(b²-4ac)] / (2a). This gives the roots of ax² + bx + c = 0. This formula always works.")
add("what is the discriminant", "Discriminant D = b² - 4ac. It determines the nature of roots:\n• D > 0: Two distinct real roots.\n• D = 0: Two equal real roots (repeated root).\n• D < 0: No real roots (complex roots).")
add("how to solve quadratic equation by factorisation", "Express the equation as product of two linear factors equal to zero. Example: x²-5x+6=0 → (x-2)(x-3)=0 → x=2 or x=3.")
add("how to solve quadratic by completing the square", """Completing the square method for ax²+bx+c=0:
1. Divide by a: x² + (b/a)x + c/a = 0
2. Move constant: x² + (b/a)x = -c/a
3. Add (b/2a)² both sides: (x + b/2a)² = (b²-4ac)/(4a²)
4. Take square root and solve for x.
Example: x²-4x-5=0 → (x-2)²=9 → x-2=±3 → x=5 or x=-1.""")
add("what is the sum and product of roots of quadratic equation", "For ax²+bx+c=0 with roots α and β:\n• Sum of roots: α + β = -b/a\n• Product of roots: α × β = c/a\nExample: x²-5x+6=0: Sum = 5/1 = 5, Product = 6/1 = 6. Roots are 2 and 3. Check: 2+3=5 ✓, 2×3=6 ✓.")
add("how to form quadratic equation from roots", "If roots are α and β: x² - (α+β)x + αβ = 0. Example: If roots are 3 and -4: x² - (3+(-4))x + (3×(-4)) = 0 → x² + x - 12 = 0.")

# ══════════════════════════════════════════════════════
# 11. ARITHMETIC PROGRESSION (AP)
# ══════════════════════════════════════════════════════
add("what is an arithmetic progression", "An Arithmetic Progression (AP) is a sequence where each term differs from the previous by a constant amount called the common difference (d). Example: 2, 5, 8, 11, ... has d = 3.")
add("what is the general term of AP", "General term (nth term) of AP: aₙ = a + (n-1)d. Where a = first term, d = common difference, n = term number. Example: AP 3,7,11...: a=3, d=4. 10th term = 3+(10-1)×4 = 3+36 = 39.")
add("what is the common difference of AP", "Common difference d = any term - previous term = a₂ - a₁ = a₃ - a₂ etc. Example: 5,8,11,14 → d = 8-5 = 3.")
add("what is the sum of n terms of AP", "Sum of first n terms of AP: Sₙ = n/2 × [2a + (n-1)d] or Sₙ = n/2 × (first term + last term). Example: Sum of first 10 terms of 1,2,3...: S₁₀ = 10/2 × (1+10) = 5×11 = 55.")
add("sum of first n natural numbers formula", "Sum of first n natural numbers: 1+2+3+...+n = n(n+1)/2. Example: 1+2+...+100 = 100×101/2 = 5050.")
add("sum of first n odd numbers", "Sum of first n odd numbers = n². Example: 1+3+5+7+9 = 5² = 25.")
add("sum of squares of first n natural numbers", "1²+2²+3²+...+n² = n(n+1)(2n+1)/6.")
add("sum of cubes of first n natural numbers", "1³+2³+3³+...+n³ = [n(n+1)/2]². Example: 1³+2³+3³ = (3×4/2)² = 6² = 36.")

# ══════════════════════════════════════════════════════
# 12. GEOMETRY — LINES AND ANGLES
# ══════════════════════════════════════════════════════
add("what is a point", "A point has no dimensions — no length, width or height. It represents an exact position in space.")
add("what is a line", "A line extends infinitely in both directions. It has no thickness and only one dimension (length).")
add("what is a line segment", "A line segment is a part of a line with two endpoints. It has a definite, measurable length.")
add("what is a ray", "A ray starts at a point and extends infinitely in one direction only.")
add("what are types of angles", """Types of Angles:
• Acute angle: less than 90°
• Right angle: exactly 90°
• Obtuse angle: between 90° and 180°
• Straight angle: exactly 180°
• Reflex angle: between 180° and 360°
• Complete angle: exactly 360°""")
add("what are complementary angles", "Two angles are complementary if their sum is 90°. Example: 30° and 60° are complementary.")
add("what are supplementary angles", "Two angles are supplementary if their sum is 180°. Example: 110° and 70° are supplementary.")
add("what are vertically opposite angles", "When two lines intersect, the angles opposite to each other are called vertically opposite angles. They are always equal.")
add("what are alternate interior angles", "When a transversal cuts two parallel lines, alternate interior angles are on opposite sides of the transversal, between the parallel lines. They are equal.")
add("what are corresponding angles", "When a transversal cuts two parallel lines, corresponding angles are on the same side of the transversal and in the same position. They are equal.")
add("what are co-interior angles", "Co-interior angles (same-side interior or consecutive interior angles) are on the same side of the transversal, between parallel lines. They are supplementary (add up to 180°).")

# ══════════════════════════════════════════════════════
# 13. TRIANGLES
# ══════════════════════════════════════════════════════
add("what is the angle sum property of triangle", "The sum of all three interior angles of a triangle is always 180°. ∠A + ∠B + ∠C = 180°.")
add("what is the exterior angle property of triangle", "An exterior angle of a triangle equals the sum of the two non-adjacent (remote) interior angles. ∠exterior = ∠A + ∠B.")
add("types of triangles by sides", """Types of triangles by sides:
• Equilateral: all 3 sides equal, all angles = 60°
• Isosceles: 2 sides equal, base angles equal
• Scalene: all 3 sides different""")
add("types of triangles by angles", """Types of triangles by angles:
• Acute triangle: all angles < 90°
• Right triangle: one angle = 90°
• Obtuse triangle: one angle > 90°""")
add("what is pythagoras theorem", "Pythagoras Theorem: In a right-angled triangle, the square of the hypotenuse equals the sum of squares of the other two sides. c² = a² + b², where c is hypotenuse. Example: 3²+4²=5² → 9+16=25 ✓.")
add("what are pythagorean triplets", "Pythagorean triplets are sets of three integers (a,b,c) satisfying a²+b²=c². Common triplets: (3,4,5), (5,12,13), (8,15,17), (7,24,25). Multiples also work: (6,8,10), (9,12,15).")
add("converse of pythagoras theorem", "Converse of Pythagoras: If c² = a²+b², then the triangle is right-angled with hypotenuse c.")
add("what is congruence of triangles", "Two triangles are congruent if they have the same shape and size (all corresponding sides and angles are equal).")
add("what are congruence criteria for triangles", """Congruence Criteria (Rules):
• SSS: All 3 sides equal
• SAS: 2 sides and included angle equal
• ASA: 2 angles and included side equal
• AAS: 2 angles and non-included side equal
• RHS: Right angle, Hypotenuse, Side (for right triangles only)""")
add("what is similarity of triangles", "Two triangles are similar if they have the same shape but not necessarily the same size. All corresponding angles are equal and corresponding sides are proportional.")
add("what are similarity criteria for triangles", """Similarity Criteria (Rules):
• AA (or AAA): 2 pairs of angles equal
• SSS: All 3 sides proportional
• SAS: 2 sides proportional and included angle equal""")
add("what is basic proportionality theorem BPT", "Basic Proportionality Theorem (Thales Theorem): If a line is drawn parallel to one side of a triangle, it divides the other two sides proportionally. If DE || BC in △ABC, then AD/DB = AE/EC.")
add("what is the area of triangle formula", """Area of Triangle formulas:
• Area = (1/2) × base × height
• Heron's formula: Area = √[s(s-a)(s-b)(s-c)], where s = (a+b+c)/2
• For equilateral triangle: Area = (√3/4) × a²
• For right triangle: Area = (1/2) × product of two legs""")
add("what is heron's formula", "Heron's Formula: Area = √[s(s-a)(s-b)(s-c)], where s = semi-perimeter = (a+b+c)/2, and a,b,c are the sides. Example: Triangle with sides 3,4,5: s=(3+4+5)/2=6. Area=√(6×3×2×1)=√36=6.")
add("medians of triangle", "A median connects a vertex to the midpoint of the opposite side. Every triangle has 3 medians. They meet at the centroid, which divides each median in 2:1 ratio.")
add("what is centroid of triangle", "The centroid is the point where all three medians of a triangle meet. It divides each median in ratio 2:1 from vertex. Centroid coordinates = ((x₁+x₂+x₃)/3, (y₁+y₂+y₃)/3).")

# ══════════════════════════════════════════════════════
# 14. QUADRILATERALS
# ══════════════════════════════════════════════════════
add("sum of angles in a quadrilateral", "The sum of interior angles of any quadrilateral is 360°.")
add("properties of parallelogram", """Properties of Parallelogram:
• Opposite sides are equal and parallel
• Opposite angles are equal
• Consecutive angles are supplementary (sum = 180°)
• Diagonals bisect each other
• Area = base × height""")
add("properties of rectangle", """Properties of Rectangle:
• All angles are 90°
• Opposite sides are equal and parallel
• Diagonals are equal and bisect each other
• Area = length × breadth
• Perimeter = 2(l + b)
• Diagonal = √(l² + b²)""")
add("properties of square", """Properties of Square:
• All sides equal, all angles 90°
• Diagonals are equal, bisect each other at 90°
• Diagonal = a√2 (where a is side)
• Area = a² or (diagonal²)/2
• Perimeter = 4a""")
add("properties of rhombus", """Properties of Rhombus:
• All sides equal
• Opposite angles equal, consecutive angles supplementary
• Diagonals bisect each other at 90° (perpendicular)
• Area = (1/2) × d₁ × d₂ (product of diagonals divided by 2)""")
add("properties of trapezium", """Properties of Trapezium:
• One pair of opposite sides is parallel (called parallel sides or bases)
• Area = (1/2) × (sum of parallel sides) × height
• Isosceles trapezium: non-parallel sides are equal, base angles equal""")

# ══════════════════════════════════════════════════════
# 15. CIRCLES
# ══════════════════════════════════════════════════════
add("what is a circle", "A circle is the set of all points equidistant from a fixed point called the centre. The distance from centre to any point on the circle is the radius.")
add("what is radius diameter chord", """Key parts of a circle:
• Radius (r): distance from centre to circle edge
• Diameter (d): longest chord passing through centre. d = 2r
• Chord: line segment joining two points on circle
• Arc: part of the circle's circumference
• Sector: 'pie slice' — region between two radii and an arc
• Segment: region between a chord and an arc""")
add("circumference of circle formula", "Circumference (perimeter) of circle = 2πr = πd. Where π ≈ 3.14159 or 22/7.")
add("area of circle formula", "Area of circle = πr². Example: radius = 7 cm, Area = π×7² = 22/7×49 = 154 cm².")
add("area of sector formula", "Area of sector = (θ/360°) × πr², where θ is the angle of sector. Length of arc = (θ/360°) × 2πr.")
add("area of ring formula", "Area of ring (annulus) = π(R² - r²), where R = outer radius, r = inner radius.")
add("what is tangent to circle", "A tangent to a circle is a line that touches the circle at exactly one point (called the point of tangency). The radius at the point of tangency is perpendicular to the tangent.")
add("how many tangents from external point", "From an external point, exactly two tangents can be drawn to a circle. Both tangents from the same external point are equal in length.")
add("what is the angle in semicircle", "The angle in a semicircle is always 90°. (Angle subtended by diameter at any point on the circle is a right angle.)")
add("angles subtended by same arc", "Angles subtended by the same arc at the circumference are equal. The angle at centre = 2 × angle at circumference.")
add("what is cyclic quadrilateral", "A cyclic quadrilateral is a quadrilateral whose all four vertices lie on a circle. Opposite angles of a cyclic quadrilateral are supplementary (sum = 180°).")

# ══════════════════════════════════════════════════════
# 16. COORDINATE GEOMETRY
# ══════════════════════════════════════════════════════
add("what is coordinate geometry", "Coordinate geometry (Cartesian geometry) uses a number system to describe points in a plane using pairs (x, y). The x-axis is horizontal, y-axis is vertical. They meet at the origin O(0,0).")
add("what are the four quadrants", """The x and y axes divide the plane into 4 quadrants:
• Quadrant I: x > 0, y > 0 (positive, positive)
• Quadrant II: x < 0, y > 0 (negative, positive)
• Quadrant III: x < 0, y < 0 (negative, negative)
• Quadrant IV: x > 0, y < 0 (positive, negative)""")
add("distance formula in coordinate geometry", "Distance between two points (x₁,y₁) and (x₂,y₂): d = √[(x₂-x₁)² + (y₂-y₁)²]. This comes from Pythagoras theorem.")
add("midpoint formula", "Midpoint of line segment joining (x₁,y₁) and (x₂,y₂): M = ((x₁+x₂)/2, (y₁+y₂)/2).")
add("section formula", "Section Formula: Point dividing (x₁,y₁) and (x₂,y₂) in ratio m:n internally: P = ((mx₂+nx₁)/(m+n), (my₂+ny₁)/(m+n)).")
add("area of triangle in coordinate geometry", "Area of triangle with vertices (x₁,y₁), (x₂,y₂), (x₃,y₃): Area = (1/2)|x₁(y₂-y₃) + x₂(y₃-y₁) + x₃(y₁-y₂)|.")
add("what is slope of a line", "Slope (gradient) m = (y₂-y₁)/(x₂-x₁) = tan θ, where θ is angle made with positive x-axis. Slope of horizontal line = 0. Slope of vertical line = undefined.")
add("equation of a straight line forms", """Equation of straight line:
• Slope-intercept form: y = mx + c (m=slope, c=y-intercept)
• Point-slope form: y - y₁ = m(x - x₁)
• Two-point form: (y-y₁)/(y₂-y₁) = (x-x₁)/(x₂-x₁)
• Intercept form: x/a + y/b = 1 (a,b are x and y intercepts)""")

# ══════════════════════════════════════════════════════
# 17. MENSURATION (Areas and Volumes)
# ══════════════════════════════════════════════════════
add("area and perimeter formulas for 2D shapes", """2D Shape Formulas:
• Square: Area=a², Perimeter=4a
• Rectangle: Area=l×b, Perimeter=2(l+b)
• Triangle: Area=(1/2)×b×h, Perimeter=a+b+c
• Equilateral Triangle: Area=(√3/4)a², Perimeter=3a
• Parallelogram: Area=b×h, Perimeter=2(a+b)
• Trapezium: Area=(1/2)(a+b)×h
• Rhombus: Area=(1/2)d₁d₂, Perimeter=4a
• Circle: Area=πr², Circumference=2πr
• Semicircle: Area=(1/2)πr², Perimeter=πr+2r""")
add("volume and surface area of 3D shapes", """3D Shape Formulas:
• Cube (side a): Volume=a³, TSA=6a², LSA=4a²
• Cuboid (l,b,h): Volume=lbh, TSA=2(lb+bh+hl), LSA=2(l+b)h
• Cylinder (r,h): Volume=πr²h, CSA=2πrh, TSA=2πr(r+h)
• Cone (r,l,h): Volume=(1/3)πr²h, CSA=πrl, TSA=πr(r+l), l=√(r²+h²)
• Sphere (r): Volume=(4/3)πr³, SA=4πr²
• Hemisphere (r): Volume=(2/3)πr³, CSA=2πr², TSA=3πr²""")
add("what is lateral surface area", "Lateral Surface Area (LSA) or Curved Surface Area (CSA) is the area of all faces excluding the top and bottom bases.")
add("what is total surface area", "Total Surface Area (TSA) includes all faces of a 3D shape — lateral faces plus top and bottom bases.")
add("frustum formulas", "Frustum (truncated cone, radii R and r, height h, slant height l): Volume=(πh/3)(R²+r²+Rr), CSA=π(R+r)l, TSA=π(R+r)l+π(R²+r²), where l=√(h²+(R-r)²).")

# ══════════════════════════════════════════════════════
# 18. TRIGONOMETRY
# ══════════════════════════════════════════════════════
add("what is trigonometry", "Trigonometry studies the relationship between angles and sides of right-angled triangles. The three main ratios are sine, cosine, and tangent.")
add("what are the trigonometric ratios", """Trigonometric Ratios (for angle θ in a right triangle):
• sin θ = Opposite / Hypotenuse = P/H
• cos θ = Adjacent / Hypotenuse = B/H
• tan θ = Opposite / Adjacent = P/B
• cosec θ = 1/sin θ = H/P
• sec θ = 1/cos θ = H/B
• cot θ = 1/tan θ = B/P
Mnemonic: SOH-CAH-TOA (Sine=Opp/Hyp, Cosine=Adj/Hyp, Tangent=Opp/Adj)""")
add("trigonometric values table", """Standard Trigonometric Values:
     0°    30°   45°   60°   90°
sin: 0     1/2   1/√2  √3/2  1
cos: 1     √3/2  1/√2  1/2   0
tan: 0     1/√3  1     √3    undefined
cosec: ∞   2     √2    2/√3  1
sec:   1   2/√3  √2    2     ∞
cot:   ∞   √3    1     1/√3  0""")
add("what are the pythagorean identities in trigonometry", """Pythagorean Trigonometric Identities:
1. sin²θ + cos²θ = 1
2. 1 + tan²θ = sec²θ
3. 1 + cot²θ = cosec²θ
These are derived from Pythagoras theorem.""")
add("what are reciprocal trigonometric identities", """Reciprocal Identities:
• sin θ × cosec θ = 1
• cos θ × sec θ = 1
• tan θ × cot θ = 1
• tan θ = sin θ / cos θ
• cot θ = cos θ / sin θ""")
add("what is angle of elevation", "The angle of elevation is the angle formed when looking UP from the horizontal to an object above. Example: the angle you look up at when seeing the top of a building.")
add("what is angle of depression", "The angle of depression is the angle formed when looking DOWN from the horizontal to an object below. It equals the angle of elevation from that object (alternate angles).")
add("how to solve height and distance problems", "Steps: 1. Draw a diagram. 2. Identify the right triangle. 3. Label the known sides/angle. 4. Use the correct trig ratio: tan θ = height/distance usually. 5. Solve for unknown. Example: If angle of elevation = 45° and distance = 50m, height = 50 × tan45° = 50 × 1 = 50m.")
add("complementary angle identities trigonometry", """Complementary Angle Identities (A + B = 90°):
• sin(90°-θ) = cosθ
• cos(90°-θ) = sinθ
• tan(90°-θ) = cotθ
• cot(90°-θ) = tanθ
• sec(90°-θ) = cosecθ
• cosec(90°-θ) = secθ""")

# ══════════════════════════════════════════════════════
# 19. STATISTICS
# ══════════════════════════════════════════════════════
add("what is mean", "Mean (Arithmetic Mean) = Sum of all observations / Total number of observations. Mean = Σx/n. Example: Mean of 4,7,2,9,3 = (4+7+2+9+3)/5 = 25/5 = 5.")
add("what is median", "Median is the middle value when data is arranged in order. If n is odd: Median = ((n+1)/2)th term. If n is even: Median = average of (n/2)th and (n/2+1)th terms. Example: 2,3,4,6,8 → Median = 4 (middle).")
add("what is mode", "Mode is the value that appears most frequently in a data set. A data set can have no mode, one mode, or multiple modes. Example: 2,3,3,4,5,3,7 → Mode = 3 (appears 3 times).")
add("mean median mode relation formula", "Empirical Relationship: Mode = 3 × Median - 2 × Mean. (This holds for moderately skewed distributions.)")
add("what is mean for grouped data", """Mean for Grouped Data:
• Direct Method: Mean = Σfᵢxᵢ / Σfᵢ (where fᵢ=frequency, xᵢ=class midpoint)
• Assumed Mean Method: Mean = a + (Σfᵢdᵢ/Σfᵢ), where dᵢ = xᵢ - a, a = assumed mean
• Step Deviation Method: Mean = a + h×(Σfᵢuᵢ/Σfᵢ), where uᵢ = dᵢ/h""")
add("what is median for grouped data", "Median for grouped data: Median = l + [(n/2 - cf)/f] × h. Where l=lower class boundary, n=total frequency, cf=cumulative frequency before median class, f=median class frequency, h=class width.")
add("what is mode for grouped data", "Mode for grouped data: Mode = l + [(f₁-f₀)/(2f₁-f₀-f₂)] × h. Where l=lower boundary of modal class, f₁=frequency of modal class, f₀=frequency before, f₂=frequency after, h=class width.")
add("what is range in statistics", "Range = Maximum value - Minimum value. It measures the spread of data.")
add("what is cumulative frequency", "Cumulative frequency is the running total of frequencies up to and including each class. It is used to draw ogives (cumulative frequency curves).")
add("what is a histogram", "A histogram is a bar graph where bars represent frequency (or frequency density) for continuous data grouped in class intervals. There are no gaps between bars.")
add("what is an ogive", "An ogive is a cumulative frequency curve. A 'less than' ogive plots cumulative frequency against upper class limits. It is used to find median, quartiles, and percentiles graphically.")

# ══════════════════════════════════════════════════════
# 20. PROBABILITY
# ══════════════════════════════════════════════════════
add("what is probability", "Probability measures how likely an event is to occur. P(event) = Number of favourable outcomes / Total number of possible outcomes. Probability ranges from 0 (impossible) to 1 (certain).")
add("what is sample space", "The sample space (S) is the set of all possible outcomes of an experiment. Example: Rolling a die → S = {1, 2, 3, 4, 5, 6}.")
add("what is an event in probability", "An event is a subset of the sample space. Example: Getting an even number when rolling a die → Event = {2, 4, 6}.")
add("what is complementary event", "The complement of event E is everything in the sample space that is NOT in E. P(E') = 1 - P(E). Example: P(not getting 6 on a die) = 1 - 1/6 = 5/6.")
add("probability formulas", """Key Probability Formulas:
• P(E) = Favourable outcomes / Total outcomes
• 0 ≤ P(E) ≤ 1
• P(E) + P(E') = 1
• P(certain event) = 1
• P(impossible event) = 0
• P(A or B) = P(A) + P(B) - P(A and B) [Addition Rule]
• For mutually exclusive events: P(A or B) = P(A) + P(B)""")
add("probability of coin toss", "When a fair coin is tossed: P(Head) = 1/2, P(Tail) = 1/2. Two coins: P(HH) = 1/4, P(HT or TH) = 2/4 = 1/2, P(TT) = 1/4.")
add("probability of dice", "When a fair die is rolled: P(any specific number) = 1/6. P(even) = 3/6 = 1/2. P(odd) = 1/2. P(prime number: 2,3,5) = 3/6 = 1/2. P(number > 4) = 2/6 = 1/3.")
add("probability of cards", "A standard deck has 52 cards: 4 suits (Hearts, Diamonds, Clubs, Spades), each with 13 cards (A,2,3,...,10,J,Q,K). P(any specific card)=1/52. P(ace)=4/52=1/13. P(heart)=13/52=1/4. P(face card: J,Q,K)=12/52=3/13.")

# ══════════════════════════════════════════════════════
# 21. POLYNOMIALS (Class 9-10)
# ══════════════════════════════════════════════════════
add("what is the remainder theorem", "Remainder Theorem: If polynomial p(x) is divided by (x-a), the remainder is p(a). Example: Divide x³+2x+1 by (x-1): remainder = p(1) = 1+2+1 = 4.")
add("what is the factor theorem", "Factor Theorem: (x-a) is a factor of polynomial p(x) if and only if p(a) = 0. Example: Check if (x-2) is factor of x²-5x+6: p(2) = 4-10+6 = 0 ✓. So (x-2) is a factor.")
add("zeros of a polynomial", "A zero (root) of polynomial p(x) is a value of x where p(x) = 0. For a quadratic ax²+bx+c, sum of zeros = -b/a, product of zeros = c/a.")
add("relationship between zeros and coefficients for cubic", "For cubic polynomial ax³+bx²+cx+d with zeros α,β,γ: α+β+γ = -b/a, αβ+βγ+γα = c/a, αβγ = -d/a.")
add("division algorithm for polynomials", "Division Algorithm: Dividend = Divisor × Quotient + Remainder. p(x) = g(x) × q(x) + r(x). Degree of r(x) < degree of g(x).")

# ══════════════════════════════════════════════════════
# BONUS: USEFUL TRICKS
# ══════════════════════════════════════════════════════
add("trick to find cube root quickly", "To find cube root of a perfect cube: The units digit of the cube root can be found from the units digit of the number: 1→1, 8→2, 7→3, 4→4, 5→5, 6→6, 3→7, 2→8, 9→9, 0→0. Then estimate the first digit from the remaining digits.")
add("trick to multiply two numbers close to 100", "To multiply numbers near 100: (100-a)(100-b) = 100(100-a-b) + ab. Example: 97×96 = (100-3)(100-4) = 100×93 + 12 = 9300+12 = 9312.")
add("trick for squaring numbers between 50 and 60", "For n between 50-59: n² = (25 + units digit) × 100 + (units digit)². Example: 56² = (25+6)×100 + 6² = 3100+36 = 3136.")
add("shortcut for percentage calculations", "Percentage shortcuts: 10% of x = x/10. 5% = half of 10%. 25% = x/4. 50% = x/2. 1% = x/100. To find 15%: find 10% + 5% (half of 10%). Example: 15% of 80 = 8+4 = 12.")
add("trick to check if number is divisible by 3 and 9", "Add all digits. If sum divisible by 3 → number divisible by 3. If sum divisible by 9 → number divisible by 9. Repeat until single digit if needed. Example: 459 → 4+5+9=18 → 1+8=9. Divisible by both 3 and 9.")
add("vedic maths multiplication trick", "Vedic Maths - Nikhilam method for multiplying numbers near a base (like 10, 100): Subtract each number from the base to get deficits. Cross subtract to get first part; multiply deficits for second part. Example: 97×96: deficits=-3,-4. Cross: 97-4=93 or 96-3=93. Multiply: (-3)×(-4)=12. Answer: 9312.")

# Final shuffle
random.shuffle(data)

output_path = "data/input_maths.txt"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(data))

print(f"Generated {len(data):,} training examples.")
print(f"Saved to {output_path}")
print(f"Total characters: {sum(len(d) for d in data):,}")
