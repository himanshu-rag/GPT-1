import random

# A target Q&A dataset representing a 10th-grade school curriculum & student helper
student_qa = [
    # Friendly / Motivational Study help
    {
        "q": "how do i study for exams",
        "a": "The best way to study is to use active recall: test yourself with flashcards, solve past 10th-grade exam papers, and explain concepts to someone else. Take a 5-minute break every 25 minutes (the Pomodoro technique)!"
    },
    {
        "q": "i am feeling stressed about my studies",
        "a": "It is completely normal to feel stressed! Take a deep breath. Break your syllabus down into small, daily targets. You have got this, just focus on one topic at a time!"
    },
    
    # 10th Grade Science (Physics, Chemistry, Biology)
    {
        "q": "what are newton's laws of motion",
        "a": "Newton has three laws: 1. An object stays at rest or in motion unless a force acts on it. 2. Force equals mass times acceleration (F=ma). 3. For every action, there is an equal and opposite reaction."
    },
    {
        "q": "what is photosynthesis",
        "a": "Photosynthesis is the process where plants use sunlight, carbon dioxide (CO2), and water (H2O) to make glucose (food) and release oxygen (O2) into the air. It happens inside the chloroplasts using chlorophyll."
    },
    {
        "q": "what is the periodic table",
        "a": "The periodic table organizes all known chemical elements by their atomic number. Columns are 'groups' (elements with similar properties) and rows are 'periods' representing electron shells."
    },
    {
        "q": "what is an acid and a base",
        "a": "An acid is a substance that releases hydrogen ions (H+) in water and has a pH below 7 (like lemon juice). A base releases hydroxide ions (OH-) and has a pH above 7 (like soap)."
    },
    {
        "q": "what is electricity",
        "a": "Electricity is the flow of electric charge, usually electrons moving through a conductor like a copper wire. It is measured in Amperes (current) and Volts (potential difference)."
    },
    
    # 10th Grade Mathematics (Algebra, Geometry, Trigonometry)
    {
        "q": "what is a quadratic equation",
        "a": "A quadratic equation is a polynomial equation of degree 2, written as ax^2 + bx + c = 0. You can solve it using the quadratic formula: x = [-b +/- sqrt(b^2 - 4ac)] / 2a."
    },
    {
        "q": "what is trigonometry",
        "a": "Trigonometry studies the relationships between the angles and sides of triangles. The three basic ratios are Sine (Opposite/Hypotenuse), Cosine (Adjacent/Hypotenuse), and Tangent (Opposite/Adjacent)."
    },
    {
        "q": "what is pythagoras theorem",
        "a": "In a right-angled triangle, the square of the hypotenuse (the longest side, c) is equal to the sum of the squares of the other two sides (a and b). The formula is: a^2 + b^2 = c^2."
    },
    
    # 10th Grade History & Social Science
    {
        "q": "what caused world war 1",
        "a": "World War 1 (1914-1918) was caused by four main factors (M-A-I-N): Militarism, Alliance systems, Imperialism, and Nationalism. The immediate trigger was the assassination of Archduke Franz Ferdinand."
    },
    {
        "q": "what was the french revolution",
        "a": "The French Revolution (1789) was a period of social and political upheaval in France. The common people overthrew the absolute monarchy of King Louis XVI, fighting for 'Liberty, Equality, and Fraternity'."
    },
    {
        "q": "what is democracy",
        "a": "Democracy is a system of government where power is vested in the people, who rule either directly or through freely elected representatives. It guarantees basic human rights and equal voting."
    }
]

def generate_dataset():
    output_path = "data/input_student.txt"
    dataset_content = ""
    
    # Repeat the 10th-grade educational corpus to ensure the model memorizes it
    for _ in range(250):
        random.shuffle(student_qa)
        for pair in student_qa:
            dataset_content += f"Question: {pair['q']}\nAnswer: {pair['a']}\n\n"
            
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(dataset_content)
    print(f"Dataset generated! Structured 10th-grade tutor Q&A written to {output_path}")

if __name__ == "__main__":
    generate_dataset()
