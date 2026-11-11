# ⚙️ Mechatronics Quiz App

A Python multiple-choice quiz for ND2 Mechatronics Engineering students. It has a console version (plain Python) and a browser version (Streamlit).

## What It Does
The app tests knowledge of important Mechatronics topics such as PLCs, sensors, actuators, control systems, hydraulics, pneumatics, electronics, CNC and CAD/CAM. It picks random questions, marks answers automatically, gives instant feedback with an explanation, and ends with a full results report and a review of the mistakes.

## Objectives
- Apply core Python concepts in a practical, useful project.
- Help ND2 Mechatronics students revise key topics.
- Give instant feedback so learners understand their mistakes.

## Features
- Welcome screen and main menu
- Choose between 1 and 50 questions (from a bank of 51)
- Randomised questions with options A, B, C and D
- Automatic marking and instant feedback with explanations
- Question progress indicator and running score
- Results: questions attempted, correct, incorrect, percentage, remark
- Review of incorrect answers with correct answers and explanations
- Restart the quiz at any time
- Input validation with clear error messages

## My Own Twist
- **Engineer Rank:** your score earns a rank from *Trainee* up to *Master Engineer*.
- **Machine-status LED:** a green, amber or red indicator shows the result like a real machine panel (running, warning or fault).
- **Review mode:** after the quiz, every wrong answer is shown again with the correct answer and explanation.
- **Web version:** the same quiz runs in a browser on phones and computers.

## Python Concepts Demonstrated
| Concept | Where (`mechatronics_quiz.py`) |
|---|---|
| Functions and `return` | `get_number_of_questions()`, `calculate_percentage()`, `get_remark()` |
| Lists | `questions`, `chosen`, `wrong_answers` |
| `for` loop | asking each question in `run_quiz()` |
| `while` loop | `pick_questions()`, `get_answer()`, main menu |
| `if` / `elif` / `else` | marking answers, `get_remark()`, menu choices |
| `int()` and `float()` | number of questions, percentage score |
| Error handling | `try` / `except ValueError` and invalid-input messages |
| Comments | throughout the code |

## Technologies Used
Python 3, Streamlit (web version), HTML/CSS (theme), GitHub.

## How to Run It
**Console version (only Python 3 is needed):**
1. Install Python 3.
2. Download `mechatronics_quiz.py`.
3. Open a terminal or command prompt in that folder.
4. Run: `python mechatronics_quiz.py`

**Web version (optional):**
```bash
pip install -r requirements.txt
streamlit run app.py
```
(`app.py` needs `mechatronics_quiz.py` in the same folder.)

## How the Quiz Works
1. Enter your name and choose **Start Quiz** from the menu.
2. Type how many questions you want (1 to 50).
3. Answer each question with A, B, C or D and see instant feedback.
4. At the end, see your score, percentage, remark, rank and a review of mistakes.
5. Choose to restart or exit.

## Sample Output
Real output from a test run:

```
===================================
       MECHATRONICS QUIZ APP
   ND2 Mechatronics Engineering
===================================
Enter your name: Favour

Welcome, Favour!

===== MAIN MENU =====
1. Start Quiz
2. How the quiz works
3. Exit
Choose an option (1-3): 1
How many questions do you want (1 to 50)? abc
Invalid input. Please type a whole number such as 10.
How many questions do you want (1 to 50)? 3

Question 1 of 3  |  Score so far: 0
What does SCADA stand for?
  A. Supervisory Control and Data Acquisition
  B. System Control and Digital Application
  C. Software Computer and Data Access
  D. Supervisory Circuit and Device Automation
Your answer (A/B/C/D): Z
Invalid answer. Please enter A, B, C or D.
Your answer (A/B/C/D): A
Correct! Well done.
Explanation: SCADA means Supervisory Control and Data Acquisition. It monitors and controls industrial processes.

  ...

===================================
        QUIZ RESULTS - Favour
===================================
Questions attempted : 3
Correct answers     : 2
Wrong answers       : 1
Percentage score    : 66.7%
Remark              : Good job! Keep practising to improve.
Engineer Rank       : Technician
Machine status      : [GREEN LED] SYSTEM RUNNING
===================================

REVIEW OF INCORRECT ANSWERS

1. Which device converts pressure into an electrical signal?
   Your answer   : B
   Correct answer: A
   Explanation   : A pressure transducer converts pressure into an electrical signal.

Restart the quiz? (Y/N): N
```

## What I Learned
While building this project I learned how to use Python lists, dictionaries, loops, conditional statements and functions together in one program. I learned how to convert data with `int()` and `float()`, how to handle errors with `try`/`except`, and how to validate user input so the program does not crash. I also learned how to organise code into small functions and how to turn a console program into a web app with Streamlit.

## Author
**Boniface Favour Elijah**
ND2 Mechatronics Engineering Technology, Yaba College of Technology
GitHub: [EleX-001](https://github.com/EleX-001)
