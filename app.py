# =====================================================================
# MECHATRONICS QUIZ APP
# ND2 Python Mini-Project - Mechatronics Engineering Technology
# Web version built with Python + Streamlit (runs in any browser).
# The console version is in mechatronics_quiz.py (plain Python).
#
# Python concepts shown in this file:
#   1. Functions and "return"          -> get_remark(), calculate_percentage() ...
#   2. Lists for storing information   -> QUESTIONS, answers, wrong_answers ...
#   3. Loops ("for" and "while")       -> pick_questions() [while], build_review() [for]
#   4. Conditionals (if/elif/else)     -> get_remark(), show_quiz_page() ...
#   5. Type conversion int()/float()   -> parse_question_count(), calculate_percentage()
#   6. Error handling                  -> try/except in parse_question_count()
#   7. Comments                        -> explained throughout
#   8. Unique feature                  -> "Engineer Rank" + machine-status LED
# =====================================================================

import random

import streamlit as st

# ---------------------------------------------------------------------
# PROJECT DETAILS (public information only)
# ---------------------------------------------------------------------
AUTHOR = "Boniface Favour Elijah"
DEPARTMENT = "Mechatronics Engineering Technology, ND2"
INSTITUTION = "Yaba College of Technology"

# ---------------------------------------------------------------------
# QUESTION BANK
# The questions live in mechatronics_quiz.py (a LIST of DICTIONARIES) so the
# console version and this web version always use the same questions.
# ---------------------------------------------------------------------
from mechatronics_quiz import questions as QUESTIONS

MAX_QUESTIONS = 50  # the user may choose between 1 and 50 questions

TOTAL_AVAILABLE = min(MAX_QUESTIONS, len(QUESTIONS))  # choosable range: 1 to 50


# =====================================================================
# SECTION 1: LOGIC FUNCTIONS (each one uses "return")
# =====================================================================
def parse_question_count(text, maximum):
    """Convert the user's text into a whole number between 1 and maximum.
    Returns (number, error_message). One of them is always None."""
    try:
        number = int(text.strip())          # data type conversion: str -> int
    except ValueError:
        # Error handling: the user typed letters, decimals or nothing
        return None, "Invalid input. Please type a whole number such as 10."
    if number < 1 or number > maximum:      # conditional statement
        return None, f"Please choose a number between 1 and {maximum}."
    return number, None


def pick_questions(bank, count):
    """Randomly pick 'count' different questions using a WHILE loop."""
    chosen_positions = []                   # list of positions already used
    while len(chosen_positions) < count:    # while loop
        position = random.randint(0, len(bank) - 1)
        if position not in chosen_positions:  # avoid repeating a question
            chosen_positions.append(position)
    return [bank[p] for p in chosen_positions]


def calculate_percentage(score, total):
    """Percentage score. float() makes sure we get decimals, not whole division."""
    if total == 0:
        return 0.0
    return float(score) / float(total) * 100.0


def get_remark(percentage):
    """Performance remark and engineer rank (the project's unique feature)."""
    if percentage >= 90:
        return "Outstanding! Master Mechatronics Engineer", "Master Engineer"
    elif percentage >= 75:
        return "Excellent work! You know your machines.", "Senior Technician"
    elif percentage >= 60:
        return "Good job! Keep practising to improve.", "Technician"
    elif percentage >= 50:
        return "Fair. Revise the topics you missed.", "Apprentice"
    else:
        return "Needs improvement. Study the explanations and try again.", "Trainee"


def led_colour(percentage):
    """Unique feature: a machine-status LED. Green = running, amber = warning, red = fault."""
    if percentage >= 60:
        return "🟢", "SYSTEM RUNNING"
    elif percentage >= 50:
        return "🟡", "WARNING"
    return "🔴", "FAULT - REVISE"


def build_review(answers):
    """Loop through all answers and return a LIST of the wrong ones."""
    wrong_answers = []
    for item in answers:                    # for loop
        if not item["correct"]:
            wrong_answers.append(item)
    return wrong_answers


# =====================================================================
# SECTION 2: SESSION STATE HELPERS (remember things between clicks)
# =====================================================================
def init_state():
    defaults = {"page": "home", "quiz": [], "index": 0, "answers": [],
                "submitted": False, "count": 10}
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def start_quiz(count):
    st.session_state.quiz = pick_questions(QUESTIONS, count)
    st.session_state.count = count
    st.session_state.index = 0
    st.session_state.answers = []
    st.session_state.submitted = False
    st.session_state.page = "quiz"


def go_home():
    st.session_state.page = "home"


# =====================================================================
# SECTION 3: LOOK AND FEEL (HTML/CSS theme)
# =====================================================================
def apply_theme():
    st.markdown(
        """
        <style>
        .hero {background: linear-gradient(135deg,#0b2545,#13315c 60%,#1b6ca8);
               padding: 26px 20px; border-radius: 16px; color: white;
               text-align: center; margin-bottom: 18px;
               border-bottom: 5px solid #f4b400;}
        .hero h1 {color: white; margin: 0; font-size: 1.9rem;}
        .hero p {color: #cfe3f5; margin: 6px 0 0 0;}
        .card {background:#f1f6fb; border-left:5px solid #1b6ca8; padding:14px;
               border-radius:10px; color:#0b2545; margin-bottom:10px;}
        .qbox {background:#0b2545; color:white; padding:16px; border-radius:12px;
               font-size:1.1rem; margin-bottom:12px;}
        div.stButton > button {width:100%; border-radius:10px; font-weight:600;
               padding:0.6rem 0;}
        </style>
        """,
        unsafe_allow_html=True,
    )


def show_header(subtitle):
    st.markdown(
        f'<div class="hero"><h1>⚙️ Mechatronics Quiz App</h1><p>{subtitle}</p></div>',
        unsafe_allow_html=True,
    )


# =====================================================================
# SECTION 4: PAGES
# =====================================================================
def show_home_page():
    show_header("ND2 Mechatronics Engineering · Test your knowledge")
    st.markdown(
        f'<div class="card"><b>Welcome, engineer!</b><br>'
        f'Answer multiple-choice questions on PLCs, sensors, actuators, control '
        f'systems and more. Get instant feedback and a full review at the end. '
        f'Choose between 1 and <b>{TOTAL_AVAILABLE}</b> questions.</div>',
        unsafe_allow_html=True,
    )
    st.subheader("📋 Main Menu")
    text = st.text_input(
        f"How many questions? (1 to {TOTAL_AVAILABLE})", value="10", key="count_input"
    )
    if st.button("▶️ Start Quiz"):
        number, error = parse_question_count(text, TOTAL_AVAILABLE)
        if error:
            st.error(error)         # invalid-input message
        else:
            start_quiz(number)
            st.rerun()
    col1, col2, col3 = st.columns(3)
    # Quick-start buttons
    if col1.button("Quick 10"):
        start_quiz(min(10, TOTAL_AVAILABLE)); st.rerun()
    if col2.button("Half bank"):
        start_quiz(max(1, TOTAL_AVAILABLE // 2)); st.rerun()
    if col3.button("Full test"):
        start_quiz(TOTAL_AVAILABLE); st.rerun()
    with st.expander("ℹ️ How the quiz works"):
        st.write(
            "1. Choose how many questions you want.\n"
            "2. Pick A, B, C or D and press **Submit Answer**.\n"
            "3. See instantly if you were right, with an explanation.\n"
            "4. At the end you get your score, rank and a review of mistakes."
        )
    st.caption(f"Built by {AUTHOR} · {DEPARTMENT} · {INSTITUTION}")


def show_quiz_page():
    quiz = st.session_state.quiz
    index = st.session_state.index
    total = len(quiz)
    question = quiz[index]
    score = sum(1 for a in st.session_state.answers if a["correct"])

    show_header(f"Question {index + 1} of {total}   ·   Score: {score}")
    st.progress(index / total)  # progress indicator

    st.markdown(f'<div class="qbox">{question["question"]}</div>', unsafe_allow_html=True)
    choice = st.radio(
        "Choose your answer:", question["options"], index=None,
        key=f"q_{index}", disabled=st.session_state.submitted,
    )

    if not st.session_state.submitted:
        if st.button("✅ Submit Answer"):
            if choice is None:
                st.warning("Please select an option (A, B, C or D) first.")
            else:
                letter = choice[0]  # first character is A, B, C or D
                correct = (letter == question["answer"])  # automatic marking
                st.session_state.answers.append({
                    "question": question["question"], "options": question["options"],
                    "chosen": letter, "answer": question["answer"],
                    "explanation": question["explanation"], "correct": correct,
                })
                st.session_state.submitted = True
                st.rerun()
    else:
        last = st.session_state.answers[-1]
        # Instant feedback
        if last["correct"]:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Wrong. Correct answer: {last['answer']}")
        st.info(f"💡 {last['explanation']}")
        label = "➡️ Next Question" if index + 1 < total else "🏁 See Results"
        if st.button(label):
            st.session_state.submitted = False
            if index + 1 < total:
                st.session_state.index += 1
            else:
                st.session_state.page = "results"
            st.rerun()
    if st.button("🏠 Quit to Menu"):
        go_home(); st.rerun()


def show_results_page():
    answers = st.session_state.answers
    attempted = len(answers)
    correct = sum(1 for a in answers if a["correct"])
    incorrect = attempted - correct
    percentage = calculate_percentage(correct, attempted)
    remark, rank = get_remark(percentage)
    led, status = led_colour(percentage)

    show_header("Final Results")
    st.markdown(f"### {led} {status}")
    st.markdown(f"## 🎖️ Engineer Rank: **{rank}**")
    c1, c2, c3 = st.columns(3)
    c1.metric("Attempted", attempted)
    c2.metric("Correct", correct)
    c3.metric("Incorrect", incorrect)
    st.metric("Percentage score", f"{percentage:.1f}%")
    st.progress(min(percentage / 100.0, 1.0))
    st.info(remark)

    wrong_answers = build_review(answers)
    st.subheader("🔍 Review of incorrect answers")
    if len(wrong_answers) == 0:
        st.success("Perfect! You have no incorrect answers.")
    else:
        for number, item in enumerate(wrong_answers, start=1):
            with st.expander(f"{number}. {item['question']}"):
                st.write(f"Your answer: **{item['chosen']}**")
                correct_text = [o for o in item["options"] if o.startswith(item["answer"])][0]
                st.write(f"Correct answer: **{correct_text}**")
                st.write(f"💡 {item['explanation']}")

    col1, col2 = st.columns(2)
    if col1.button("🔄 Restart Quiz"):
        start_quiz(st.session_state.count); st.rerun()
    if col2.button("🏠 Main Menu"):
        go_home(); st.rerun()


# =====================================================================
# SECTION 5: MAIN PROGRAM
# =====================================================================
def main():
    st.set_page_config(page_title="Mechatronics Quiz App", page_icon="⚙️")
    init_state()
    apply_theme()
    page = st.session_state.page
    if page == "home":
        show_home_page()
    elif page == "quiz":
        show_quiz_page()
    elif page == "results":
        show_results_page()
    else:
        go_home()


main()
