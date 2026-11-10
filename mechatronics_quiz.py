# ==========================================
# MECHATRONICS QUIZ APP
# A multiple-choice quiz for Mechatronics Engineering students.
# ==========================================

# Each question is stored as a dictionary inside a list.
questions = [
    {
        "question": "What does PLC stand for?",
        "options": [
            "A. Programmable Logic Controller",
            "B. Power Line Computer",
            "C. Program Level Circuit",
            "D. Personal Logic Control"
        ],
        "answer": "A",
        "explanation": "PLC means Programmable Logic Controller."
    },
    {
        "question": "Which device is used to detect temperature?",
        "options": [
            "A. Motor",
            "B. Thermocouple",
            "C. Gear",
            "D. Relay"
        ],
        "answer": "B",
        "explanation": "A thermocouple is used to measure temperature."
    },
    {
        "question": "What is the main function of a sensor?",
        "options": [
            "A. To produce sound",
            "B. To store energy",
            "C. To detect changes in the environment",
            "D. To generate electricity"
        ],
        "answer": "C",
        "explanation": "Sensors detect changes in physical conditions."
    },
    {
        "question": "What does CNC stand for?",
        "options": [
            "A. Computer Numerical Control",
            "B. Central Network Control",
            "C. Computer Network Circuit",
            "D. Controlled Number Calculation"
        ],
        "answer": "A",
        "explanation": "CNC means Computer Numerical Control."
    },
    {
        "question": "Which component converts electrical energy into mechanical motion?",
        "options": [
            "A. Sensor",
            "B. Actuator",
            "C. Resistor",
            "D. Capacitor"
        ],
        "answer": "B",
        "explanation": "An actuator converts energy into physical movement."
    },
    {
        "question": "Which of these is an example of an automation system?",
        "options": [
            "A. Automatic washing machine",
            "B. Manual broom",
            "C. Ordinary chair",
            "D. Notebook"
        ],
        "answer": "A",
        "explanation": "An automatic washing machine performs tasks automatically."
    },
    {
        "question": "What is the brain of a PLC?",
        "options": [
            "A. Power supply",
            "B. CPU",
            "C. Input terminal",
            "D. Output terminal"
        ],
        "answer": "B",
        "explanation": "The CPU processes instructions in a PLC."
    },
    {
        "question": "Which machine is commonly used in robotics?",
        "options": [
            "A. Robotic arm",
            "B. Hand saw",
            "C. Wheelbarrow",
            "D. Hammer"
        ],
        "answer": "A",
        "explanation": "A robotic arm performs automated movements."
    },
    {
        "question": "What does CAD stand for?",
        "options": [
            "A. Computer Aided Design",
            "B. Central Automatic Device",
            "C. Control And Development",
            "D. Computer Applied Data"
        ],
        "answer": "A",
        "explanation": "CAD means Computer Aided Design."
    },
    {
        "question": "Which of these is an input device?",
        "options": [
            "A. Motor",
            "B. Lamp",
            "C. Sensor",
            "D. Speaker"
        ],
        "answer": "C",
        "explanation": "A sensor provides input to a control system."
    }
]


# FUNCTION 1: Allow the student to choose the number of questions.
# It returns the number selected by the student.
def choose_quiz_length():
    print("\nChoose the number of questions:")
    print("1. Five questions")
    print("2. Ten questions")

    while True:
        try:
            choice = int(input("Enter 1 or 2: "))

            if choice == 1:
                return 5
            elif choice == 2:
                return 10
            else:
                print("Invalid choice. Please enter 1 or 2.")

        except ValueError:
            print("Please enter a number, either 1 or 2.")


# FUNCTION 2: Get and validate the student's answer.
# It returns a valid answer (A, B, C or D).
def get_answer():
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer in ["A", "B", "C", "D"]:
            return answer
        else:
            print("Invalid answer. Please choose A, B, C or D.")


# FUNCTION 3: Calculate the student's percentage.
# It returns the percentage as a value.
def calculate_percentage(score, total):
    return (score / total) * 100


# FUNCTION 4: Run the quiz and check the student's answers.
# It returns the score and a list of incorrect answers.
def run_quiz(selected_questions):
    score = 0
    wrong_answers = []

    # Loop through each selected question.
    for question in selected_questions:
        print("\n" + question["question"])

        # Display all the available options.
        for option in question["options"]:
            print(option)

        # Collect the student's answer.
        answer = get_answer()

        # Check whether the answer is correct.
        if answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer!")
            print("Correct answer:", question["answer"])

            # Store incorrectly answered questions for review.
            wrong_answers.append(question)

        print("Explanation:", question["explanation"])

    return score, wrong_answers


# FUNCTION 5: Display the final result and review wrong answers.
def show_result(name, score, total, wrong_answers):
    percentage = calculate_percentage(score, total)

    print("\n================================")
    print("          QUIZ RESULT")
    print("================================")

    print("Student Name:", name)
    print("Score:", score, "out of", total)
    print("Percentage:", round(percentage, 2), "%")

    # Grade the student's performance.
    if percentage >= 70:
        print("Excellent performance!")
    elif percentage >= 50:
        print("Good effort! Keep studying.")
    else:
        print("Keep practising. You can improve!")

    # Review questions answered incorrectly.
    if len(wrong_answers) > 0:
        print("\n===== INCORRECT ANSWER REVIEW =====")

        for question in wrong_answers:
            print("\nQuestion:", question["question"])
            print("Correct answer:", question["answer"])
            print("Explanation:", question["explanation"])

    else:
        print("\nCongratulations! You answered every question correctly.")


# MAIN FUNCTION: Controls how the whole program runs.
def main():
    print("================================")
    print("     MECHATRONICS QUIZ APP")
    print("================================")

    # Collect the student's name.
    name = input("Enter your name: ").strip()

    if name == "":
        name = "Student"

    print("\nWelcome", name)
    print("Test your knowledge of Mechatronics Engineering!")

    # Allow the student to choose five or ten questions.
    number = choose_quiz_length()

    # Select the requested number of questions from the list.
    selected_questions = questions[:number]

    print("\nAnswer the following questions.")
    print("Choose A, B, C or D.")

    # Run the quiz and collect the results.
    score, wrong_answers = run_quiz(selected_questions)

    # Display the final result.
    show_result(name, score, len(selected_questions), wrong_answers)

    print("\nThank you for using the Mechatronics Quiz App!")


# Start the program by calling the main function.
if __name__ == "__main__":
    main()
