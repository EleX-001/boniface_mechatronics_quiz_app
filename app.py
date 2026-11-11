# =====================================================================
# MECHATRONICS QUIZ APP
# ND2 Python Mini-Project - Mechatronics Engineering Technology
# Built with Python + Streamlit (runs in any browser: Android, iPhone, PC)
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
AUTHOR = "Boniface"
DEPARTMENT = "Mechatronics Engineering Technology, ND2"
INSTITUTION = "Yaba College of Technology"

# ---------------------------------------------------------------------
# QUESTION BANK
# A LIST of DICTIONARIES. Each dictionary holds one question, its four
# options, the correct letter and a short explanation.
# ---------------------------------------------------------------------
QUESTIONS = [
    {
        "question": "What does PLC stand for?",
        "options": ["A. Programmable Logic Controller", "B. Power Line Computer", "C. Program Level Circuit", "D. Personal Logic Control"],
        "answer": "A",
        "explanation": "PLC means Programmable Logic Controller. It controls machines and industrial processes."
    },
    {
        "question": "Which device detects physical changes?",
        "options": ["A. Actuator", "B. Sensor", "C. Motor", "D. Relay"],
        "answer": "B",
        "explanation": "A sensor detects changes such as temperature, pressure and movement."
    },
    {
        "question": "What is the full meaning of CNC?",
        "options": ["A. Computer Numerical Control", "B. Central Network Control", "C. Computer Number Connection", "D. Controlled Numerical Circuit"],
        "answer": "A",
        "explanation": "CNC means Computer Numerical Control."
    },
    {
        "question": "Which device converts electrical energy into mechanical energy?",
        "options": ["A. Generator", "B. Transformer", "C. Electric motor", "D. Sensor"],
        "answer": "C",
        "explanation": "An electric motor converts electrical energy into mechanical energy."
    },
    {
        "question": "What is automation?",
        "options": ["A. Manual operation of machines", "B. Use of technology to perform tasks automatically", "C. Repairing machines", "D. Stopping production"],
        "answer": "B",
        "explanation": "Automation uses technology to perform tasks with little human intervention."
    },
    {
        "question": "Which component detects temperature?",
        "options": ["A. Thermistor", "B. Gear", "C. Pulley", "D. Bearing"],
        "answer": "A",
        "explanation": "A thermistor is a temperature-sensitive resistor."
    },
    {
        "question": "What is the main function of an actuator?",
        "options": ["A. Store information", "B. Produce physical movement", "C. Measure voltage", "D. Display data"],
        "answer": "B",
        "explanation": "An actuator converts energy into physical movement."
    },
    {
        "question": "Which machine is commonly used for drilling holes?",
        "options": ["A. Lathe", "B. Milling machine", "C. Drilling machine", "D. Grinding machine"],
        "answer": "C",
        "explanation": "A drilling machine produces holes in materials."
    },
    {
        "question": "What does CAD stand for?",
        "options": ["A. Computer Aided Design", "B. Control Automatic Device", "C. Computer Applied Data", "D. Central Access Design"],
        "answer": "A",
        "explanation": "CAD means Computer Aided Design."
    },
    {
        "question": "What does CAM stand for?",
        "options": ["A. Computer Aided Manufacturing", "B. Central Automatic Machine", "C. Computer Access Management", "D. Control Applied Mechanics"],
        "answer": "A",
        "explanation": "CAM means Computer Aided Manufacturing."
    },
    {
        "question": "Which device converts mechanical energy into electrical energy?",
        "options": ["A. Motor", "B. Generator", "C. Actuator", "D. Pump"],
        "answer": "B",
        "explanation": "A generator converts mechanical energy into electrical energy."
    },
    {
        "question": "What is a robot?",
        "options": ["A. A manually operated tool", "B. A programmable machine that performs tasks", "C. A measuring instrument", "D. A keyboard"],
        "answer": "B",
        "explanation": "A robot is a programmable machine capable of carrying out tasks."
    },
    {
        "question": "Which of these is a hydraulic fluid?",
        "options": ["A. Water only", "B. Hydraulic oil", "C. Petrol", "D. Kerosene"],
        "answer": "B",
        "explanation": "Hydraulic oil transmits power in hydraulic systems."
    },
    {
        "question": "What is the function of a gear?",
        "options": ["A. Transmit rotary motion and torque", "B. Measure temperature", "C. Store electricity", "D. Detect light"],
        "answer": "A",
        "explanation": "Gears transmit rotary motion and torque between shafts."
    },
    {
        "question": "Which instrument measures electrical current?",
        "options": ["A. Voltmeter", "B. Ammeter", "C. Thermometer", "D. Barometer"],
        "answer": "B",
        "explanation": "An ammeter measures electric current."
    },
    {
        "question": "What is the unit of electrical resistance?",
        "options": ["A. Volt", "B. Ampere", "C. Ohm", "D. Watt"],
        "answer": "C",
        "explanation": "The ohm is the SI unit of electrical resistance."
    },
    {
        "question": "Which instrument measures voltage?",
        "options": ["A. Ammeter", "B. Voltmeter", "C. Speedometer", "D. Tachometer"],
        "answer": "B",
        "explanation": "A voltmeter measures electrical potential difference."
    },
    {
        "question": "What is the function of a relay?",
        "options": ["A. Switch an electrical circuit", "B. Measure pressure", "C. Produce sound", "D. Store energy"],
        "answer": "A",
        "explanation": "A relay is an electrically operated switch."
    },
    {
        "question": "Which logic gate gives an output of 1 only when all inputs are 1?",
        "options": ["A. OR", "B. NOT", "C. AND", "D. NOR"],
        "answer": "C",
        "explanation": "An AND gate produces 1 only when all its inputs are 1."
    },
    {
        "question": "Which logic gate reverses its input?",
        "options": ["A. AND", "B. OR", "C. NOT", "D. XOR"],
        "answer": "C",
        "explanation": "A NOT gate changes 1 to 0 and 0 to 1."
    },
    {
        "question": "What does SCADA stand for?",
        "options": ["A. Supervisory Control and Data Acquisition", "B. System Control and Digital Application", "C. Software Computer and Data Access", "D. Supervisory Circuit and Device Automation"],
        "answer": "A",
        "explanation": "SCADA monitors and controls industrial processes."
    },
    {
        "question": "Which component stores electrical energy?",
        "options": ["A. Capacitor", "B. Switch", "C. Fuse", "D. Relay"],
        "answer": "A",
        "explanation": "A capacitor stores electrical energy in an electric field."
    },
    {
        "question": "What is torque?",
        "options": ["A. Turning effect of a force", "B. Resistance to electricity", "C. Speed of light", "D. Temperature"],
        "answer": "A",
        "explanation": "Torque is the turning effect produced by a force."
    },
    {
        "question": "Which material is a good electrical conductor?",
        "options": ["A. Rubber", "B. Plastic", "C. Copper", "D. Wood"],
        "answer": "C",
        "explanation": "Copper allows electric current to flow easily."
    },
    {
        "question": "What is the function of a fuse?",
        "options": ["A. Increase voltage", "B. Protect a circuit from excessive current", "C. Store current", "D. Measure resistance"],
        "answer": "B",
        "explanation": "A fuse melts and breaks a circuit when excessive current flows."
    },
    {
        "question": "Which device converts pressure into an electrical signal?",
        "options": ["A. Pressure transducer", "B. Gearbox", "C. Pulley", "D. Bearing"],
        "answer": "A",
        "explanation": "A pressure transducer converts pressure into an electrical signal."
    },
    {
        "question": "What is the SI unit of force?",
        "options": ["A. Joule", "B. Newton", "C. Watt", "D. Pascal"],
        "answer": "B",
        "explanation": "The newton is the SI unit of force."
    },
    {
        "question": "Which system uses pressurised liquid to transmit power?",
        "options": ["A. Pneumatic", "B. Hydraulic", "C. Electrical", "D. Mechanical"],
        "answer": "B",
        "explanation": "Hydraulic systems transmit power using pressurised liquids."
    },
    {
        "question": "Which system uses compressed air?",
        "options": ["A. Hydraulic", "B. Pneumatic", "C. Electrical", "D. Magnetic"],
        "answer": "B",
        "explanation": "Pneumatic systems use compressed air to transmit power."
    },
    {
        "question": "What is a microcontroller?",
        "options": ["A. A small computer on a single chip", "B. A mechanical gear", "C. A hydraulic pump", "D. A battery"],
        "answer": "A",
        "explanation": "A microcontroller is a small computer integrated into a single chip."
    },
    {
        "question": "Which device converts light into an electrical signal?",
        "options": ["A. Photodiode", "B. Thermistor", "C. Relay", "D. Motor"],
        "answer": "A",
        "explanation": "A photodiode detects light and produces an electrical response."
    },
    {
        "question": "What is the purpose of a bearing?",
        "options": ["A. Support rotating shafts and reduce friction", "B. Increase voltage", "C. Measure temperature", "D. Store data"],
        "answer": "A",
        "explanation": "Bearings support moving parts and reduce friction."
    },
    {
        "question": "Which of these is an input device?",
        "options": ["A. Motor", "B. Sensor", "C. Lamp", "D. Speaker"],
        "answer": "B",
        "explanation": "A sensor provides input information to a control system."
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Computer Power Unit", "C. Control Program Utility", "D. Central Programming User"],
        "answer": "A",
        "explanation": "CPU means Central Processing Unit."
    },
    {
        "question": "Which of these is a renewable energy source?",
        "options": ["A. Coal", "B. Petrol", "C. Solar energy", "D. Diesel"],
        "answer": "C",
        "explanation": "Solar energy comes from sunlight and is renewable."
    },
    {
        "question": "What is friction?",
        "options": ["A. A force that opposes motion", "B. A type of electricity", "C. A source of light", "D. A machine"],
        "answer": "A",
        "explanation": "Friction opposes movement between surfaces in contact."
    },
    {
        "question": "Which machine changes rotational speed?",
        "options": ["A. Gearbox", "B. Thermometer", "C. Sensor", "D. Fuse"],
        "answer": "A",
        "explanation": "A gearbox changes rotational speed and torque."
    },
    {
        "question": "What is feedback in a control system?",
        "options": ["A. Returning output information to the controller", "B. Removing sensors", "C. Stopping electricity", "D. Increasing weight"],
        "answer": "A",
        "explanation": "Feedback sends information about the output back to the controller."
    },
    {
        "question": "Which control system operates without feedback?",
        "options": ["A. Closed-loop", "B. Open-loop", "C. Feedback control", "D. Adaptive control"],
        "answer": "B",
        "explanation": "An open-loop system operates without output feedback."
    },
    {
        "question": "Which control system uses feedback?",
        "options": ["A. Open-loop", "B. Closed-loop", "C. Manual-only", "D. Passive-only"],
        "answer": "B",
        "explanation": "A closed-loop system uses feedback to regulate its output."
    },
    {
        "question": "What is the main purpose of a transformer?",
        "options": ["A. Change AC voltage levels", "B. Store mechanical energy", "C. Produce compressed air", "D. Measure temperature"],
        "answer": "A",
        "explanation": "A transformer increases or decreases alternating-current voltage."
    },
    {
        "question": "What is the SI unit of power?",
        "options": ["A. Newton", "B. Watt", "C. Ohm", "D. Pascal"],
        "answer": "B",
        "explanation": "The watt is the SI unit of power."
    },
    {
        "question": "Which component protects a motor from excessive current?",
        "options": ["A. Thermal overload relay", "B. Pulley", "C. Gear", "D. Capacitor"],
        "answer": "A",
        "explanation": "A thermal overload relay protects motors against excessive current."
    },
    {
        "question": "What does IoT stand for?",
        "options": ["A. Internet of Things", "B. Input of Technology", "C. Internal Operating Tool", "D. Internet of Terminals"],
        "answer": "A",
        "explanation": "IoT connects physical devices through networks."
    },
    {
        "question": "Which programming language is commonly used with Arduino?",
        "options": ["A. C/C++", "B. HTML only", "C. SQL only", "D. CSS only"],
        "answer": "A",
        "explanation": "Arduino programming is based on C/C++."
    },
    {
        "question": "What is the purpose of an encoder?",
        "options": ["A. Measure position or speed", "B. Produce hydraulic pressure", "C. Increase temperature", "D. Store fuel"],
        "answer": "A",
        "explanation": "An encoder provides information about position, direction or speed."
    },
    {
        "question": "Which of these is an example of an actuator?",
        "options": ["A. Electric motor", "B. Thermistor", "C. Photodiode", "D. Voltmeter"],
        "answer": "A",
        "explanation": "An electric motor produces mechanical movement."
    },
    {
        "question": "What is the main function of a PLC input module?",
        "options": ["A. Receive signals from input devices", "B. Display pictures", "C. Produce force", "D. Store hydraulic oil"],
        "answer": "A",
        "explanation": "A PLC input module receives signals from input devices such as sensors and switches."
    },
    # ------------------------------------------------------------------
    # NOTE: the two questions below (49 and 50) were ADDED so the bank
    # reaches 50. The original 49 and 50 were cut off when the code was
    # shared. Replace these two with your own originals if you wish.
    # ------------------------------------------------------------------
    {
        "question": "What does PWM stand for in motor control?",
        "options": ["A. Pulse Width Modulation", "B. Power Wire Management", "C. Programmable Wave Motor", "D. Phase Winding Method"],
        "answer": "A",
        "explanation": "PWM (Pulse Width Modulation) controls motor speed by switching power on and off very quickly."
    },
    {
        "question": "What is the purpose of a limit switch?",
        "options": ["A. Detect when a moving part reaches a set position", "B. Measure temperature", "C. Store electrical energy", "D. Generate sound"],
        "answer": "A",
        "explanation": "A limit switch is triggered when a moving part reaches a set position, so machines can stop or reverse."
    },
]

TOTAL_AVAILABLE = len(QUESTIONS)  # how many questions exist in the bank


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
        f'The bank has <b>{TOTAL_AVAILABLE}</b> questions.</div>',
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
