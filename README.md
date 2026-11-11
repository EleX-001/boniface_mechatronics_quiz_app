# ⚙️ Mechatronics Quiz App

A browser-based multiple-choice quiz for ND2 Mechatronics Engineering students, built with Python and Streamlit.

## Project Description
The app tests knowledge of core Mechatronics topics such as PLCs, sensors, actuators, control systems, hydraulics, pneumatics, electronics and CNC. It marks answers automatically, gives instant feedback with explanations, and ends with a full results report. It works on Android phones, iPhones and computers through a web browser.

## Objectives
- Apply core Python concepts in a practical, useful project.
- Help ND2 Mechatronics students revise key topics.
- Provide instant feedback so learners understand their mistakes.

## Features
- Welcome screen and main menu with a Mechatronics theme
- Choose 1 to 50 questions (with input validation)
- Randomised questions, options A, B, C and D
- Automatic marking and instant feedback with explanation
- Question progress indicator and running score
- Final results: attempted, correct, incorrect, percentage, remark
- Review of incorrect answers with correct answers and explanations
- Restart the quiz at any time
- **Unique feature:** Engineer Rank (Trainee to Master Engineer) and a machine-status LED (green / amber / red)

## Python Concepts Demonstrated
| Concept | Where in `app.py` |
|---|---|
| Functions and `return` | `parse_question_count()`, `calculate_percentage()`, `get_remark()` |
| Lists | `QUESTIONS`, `answers`, `wrong_answers` |
| `for` loop | `build_review()` |
| `while` loop | `pick_questions()` |
| `if` / `elif` / `else` | `get_remark()`, `led_colour()`, page routing |
| `int()` and `float()` | `parse_question_count()`, `calculate_percentage()` |
| Error handling | `try` / `except ValueError` and invalid-input messages |
| Comments | Throughout the code |

## Technologies Used
Python 3, Streamlit, HTML/CSS (theme), GitHub, Streamlit Community Cloud.

## How to Install and Run
```bash
git clone https://github.com/EleX-001/boniface_mechatronics_quiz_app.git
cd boniface_mechatronics_quiz_app
pip install -r requirements.txt
streamlit run app.py
```
Then open the local address shown in the terminal.

## How the Quiz Works
1. Enter how many questions you want (1 to 50) and press **Start Quiz**.
2. Choose A, B, C or D and press **Submit Answer**.
3. See instantly whether you were right, plus an explanation.
4. Press **Next** until the end, then view your score, rank and review.
5. Press **Restart Quiz** to try again with new random questions.

## Author
Boniface, ND2 Mechatronics Engineering Technology, Yaba College of Technology.
GitHub: [EleX-001](https://github.com/EleX-001)
