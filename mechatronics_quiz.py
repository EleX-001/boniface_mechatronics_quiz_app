
import random

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
        "options": [
            "A. Computer Numerical Control",
            "B. Central Network Control",
            "C. Computer Number Connection",
            "D. Controlled Numerical Circuit"
        ],
        "answer": "A",
        "explanation": "CNC means Computer Numerical Control. It controls machine tools using programmed instructions."
    },
    {
        "question": "Which of these converts electrical energy into mechanical energy?",
        "options": ["A. Generator", "B. Transformer", "C. Electric motor", "D. Sensor"],
        "answer": "C",
        "explanation": "An electric motor converts electrical energy into mechanical energy."
    },
    {
        "question": "What is automation?",
        "options": [
            "A. Manual operation of machines",
            "B. Use of technology to perform tasks automatically",
            "C. Repairing machines",
            "D. Stopping production"
        ],
        "answer": "B",
        "explanation": "Automation uses machines and control systems to perform tasks with little human intervention."
    },
    {
        "question": "Which component is used to detect temperature?",
        "options": ["A. Thermistor", "B. Gear", "C. Pulley", "D. Bearing"],
        "answer": "A",
        "explanation": "A thermistor is a temperature-sensitive resistor."
    },
    {
        "question": "What is the main function of an actuator?",
        "options": [
            "A. Store information",
            "B. Produce physical movement",
            "C. Measure voltage",
            "D. Display data"
        ],
        "answer": "B",
        "explanation": "An actuator converts energy into physical movement."
    },
    {
        "question": "Which machine is commonly used for drilling holes?",
        "options": ["A. Lathe", "B. Milling machine", "C. Drilling machine", "D. Grinding machine"],
        "answer": "C",
        "explanation": "A drilling machine is designed to produce holes in materials."
    },
    {
        "question": "What does CAD stand for?",
        "options": [
            "A. Computer Aided Design",
            "B. Control Automatic Device",
            "C. Computer Applied Data",
            "D. Central Access Design"
        ],
        "answer": "A",
        "explanation": "CAD means Computer Aided Design. It is used to create technical drawings and models."
    },
    {
        "question": "What does CAM stand for?",
        "options": [
            "A. Computer Aided Manufacturing",
            "B. Central Automatic Machine",
            "C. Computer Access Management",
            "D. Control Applied Mechanics"
        ],
        "answer": "A",
        "explanation": "CAM means Computer Aided Manufacturing. It uses computers to assist manufacturing."
    },
    {
        "question": "Which device converts mechanical energy into electrical energy?",
        "options": ["A. Motor", "B. Generator", "C. Actuator", "D. Pump"],
        "answer": "B",
        "explanation": "A generator converts mechanical energy into electrical energy."
    },
    {
        "question": "What is a robot?",
        "options": [
            "A. A manually operated tool",
            "B. A programmable machine that performs tasks",
            "C. A measuring instrument",
            "D. A type of computer keyboard"
        ],
        "answer": "B",
        "explanation": "A robot is a programmable machine capable of carrying out tasks automatically."
    },
    {
        "question": "Which of these is a hydraulic fluid?",
        "options": ["A. Water only", "B. Hydraulic oil", "C. Petrol", "D. Kerosene"],
        "answer": "B",
        "explanation": "Hydraulic oil transmits power in hydraulic systems."
    },
    {
        "question": "What is the function of a gear?",
        "options": [
            "A. Transmit rotary motion and torque",
            "B. Measure temperature",
            "C. Store electricity",
            "D. Detect light"
        ],
        "answer": "A",
        "explanation": "Gears transmit rotary motion and torque between rotating shafts."
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
        "options": [
            "A. Switch an electrical circuit",
            "B. Measure pressure",
            "C. Produce sound",
            "D. Store mechanical energy"
        ],
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
        "options": [
            "A. Supervisory Control and Data Acquisition",
            "B. System Control and Digital Application",
            "C. Software Computer and Data Access",
            "D. Supervisory Circuit and Device Automation"
        ],
        "answer": "A",
        "explanation": "SCADA means Supervisory Control and Data Acquisition. It monitors and controls industrial processes."
    },
    {
        "question": "Which component stores electrical energy?",
        "options": ["A. Capacitor", "B. Switch", "C. Fuse", "D. Relay"],
        "answer": "A",
        "explanation": "A capacitor stores electrical energy in an electric field."
    },
    {
        "question": "What is torque?",
        "options": [
            "A. A turning effect of a force",
            "B. Resistance to electricity",
            "C. Speed of light",
            "D. Temperature of a machine"
        ],
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
        "options": [
            "A. Increase voltage",
            "B. Protect a circuit from excessive current",
            "C. Store current",
            "D. Measure resistance"
        ],
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
        "options": [
            "A. A small computer on a single chip",
            "B. A mechanical gear",
            "C. A hydraulic pump",
            "D. A type of battery"
        ],
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
        "options": [
            "A. Support rotating shafts and reduce friction",
            "B. Increase electrical voltage",
            "C. Measure temperature",
            "D. Store data"
        ],
        "answer": "A",
        "explanation": "Bearings support moving parts and reduce friction."
    },
    {
        "question": "Which of these is an example of an input device?",
        "options": ["A. Motor", "B. Sensor", "C. Lamp", "D. Speaker"],
        "answer": "B",
        "explanation": "A sensor provides input information to a control system."
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Power Unit",
            "C. Control Program Utility",
            "D. Central Programming User"
        ],
        "answer": "A",
        "explanation": "CPU means Central Processing Unit. It processes instructions in a computer."
    },
    {
        "question": "Which of these is a renewable energy source?",
        "options": ["A. Coal", "B. Petrol", "C. Solar energy", "D. Diesel"],
        "answer": "C",
        "explanation": "Solar energy comes from sunlight and is renewable."
    },
    {
        "question": "What is friction?",
        "options": [
            "A. A force that opposes motion",
            "B. A type of electricity",
            "C. A source of light",
            "D. A turning machine"
        ],
        "answer": "A",
        "explanation": "Friction is a force that opposes movement between surfaces in contact."
    },
    {
        "question": "Which machine is used to reduce or increase rotational speed?",
        "options": ["A. Gearbox", "B. Thermometer", "C. Sensor", "D. Fuse"],
        "answer": "A",
        "explanation": "A gearbox changes rotational speed and torque."
    },
    {
        "question": "What is feedback in a control system?",
        "options": [
            "A. Returning output information to the controller",
            "B. Removing all sensors",
            "C. Stopping electricity",
            "D. Increasing machine weight"
        ],
        "answer": "A",
        "explanation": "Feedback sends information about the output back to the controller."
    },
    {
        "question": "Which control system operates without feedback?",
        "options": ["A. Closed-loop", "B. Open-loop", "C. Feedback control", "D. Adaptive control"],
        "answer": "B",
        "explanation": "An open-loop system operates without using output feedback."
    },
    {
        "question": "Which control system uses feedback?",
        "options": ["A. Open-loop", "B. Closed-loop", "C. Manual-only", "D. Passive-only"],
        "answer": "B",
        "explanation": "A closed-loop system uses feedback to regulate its output."
    },
    {
        "question": "What is the main purpose of a transformer?",
        "options": [
            "A. Change AC voltage levels",
            "B. Store mechanical energy",
            "C. Produce compressed air",
            "D. Measure temperature"
        ],
        "answer": "A",
        "explanation": "A transformer increases or decreases alternating-current voltage."
    },
    {
        "question": "What is the unit of power?",
        "options": ["A. Newton", "B. Watt", "C. Ohm", "D. Pascal"],
        "answer": "B",
        "explanation": "The watt is the SI unit of power."
    },
    {
        "question": "Which component protects a machine from overheating?",
        "options": ["A. Thermal overload relay", "B. Pulley", "C. Gear", "D. Capacitor"],
        "answer": "A",
        "explanation": "A thermal overload relay protects motors against excessive current and overheating."
    },
    {
        "question": "What does IoT stand for?",
        "options": [
            "A. Internet of Things",
            "B. Input of Technology",
            "C. Internal Operating Tool",
            "D. Internet of Terminals"
        ],
        "answer": "A",
        "explanation": "IoT means Internet of Things. It connects physical devices through networks."
    },
    {
        "question": "Which programming language is commonly used with Arduino?",
        "options": ["A. C/C++", "B. HTML only", "C. SQL only", "D. CSS only"],
        "answer": "A",
        "explanation": "Arduino programming is based on C/C++."
    },
    {
        "question": "What is the purpose of an encoder?",
        "options": [
            "A. Measure position or speed",
            "B. Produce hydraulic pressure",
            "C. Increase temperature",
            "D. Store fuel"
        ],
        "answer": "A",
        "explanation": "An encoder provides information about position, direction or speed."
    },
    {
        "question": "Which of these is a mechanical actuator?",
        "options": ["A. Electric motor", "B. Thermistor", "C. Photodiode", "D. Voltmeter"],
        "answer": "A",
        "explanation": "An electric motor produces mechanical movement."
    },
    {
        "question": "What is the main function of a PLC input module?",
        "options": [
            "A. Receive signals from input devices",
            "B. Display pictures",
            "C. Produce mechanical force",
            "D. Store hydraulic oil"
        ],
        "answer": "A",
        "explanation": "The input module receives signals from sensors and switches."
    },
    {
        "question": "What is the main function of a PLC output module?",
        "options": [
            "A. Receive sensor signals",
            "B. Send control signals to output devices",
            "C. Measure room temperature only",
            "D. Store programs permanently only"
        ],
        "answer": "B",
        "explanation": "The output module sends signals to devices such as motors, lamps and valves."
    },
    {
        "question": "Which manufacturing process removes material using a cutting tool?",
        "options": ["A. Casting", "B. Machining", "C. Forging", "D. Welding"],
        "answer": "B",
        "explanation": "Machining removes unwanted material to achieve a required shape."
    },
    {
        "question": "What is the purpose of preventive maintenance?",
        "options": [
            "A. Wait until a machine breaks down",
            "B. Reduce the chance of equipment failure",
            "C. Increase machine breakdown",
            "D. Stop all production permanently"
        ],
        "answer": "B",
        "explanation": "Preventive maintenance involves regular servicing to reduce unexpected failures."
    }
]


def start_quiz():
    score = 0
    random.shuffle(questions)

    print("\n===================================")
    print("       MECHATRONICS QUIZ APP")
    print("===================================")
    print("Answer each question using A, B, C or D.")
    print("-----------------------------------")

    for number, q in enumerate(questions, start=1):
        print(f"\nQuestion {number}: {q['question']}")

        for option in q["options"]:
            print(option)

        while True:
            answer = input("Your answer: ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break
            print("Invalid answer. Please enter A, B, C or D.")

        if answer == q["answer"]:
            print("Correct! Well done.")
            score += 1
        else:
            print("Wrong!")
            print("Correct answer:", q["answer"])

        print("Explanation:", q["explanation"])

    percentage = (score / len(questions)) * 100

    print("\n===================================")
    print("           QUIZ RESULTS")
    print("===================================")
    print(f"Total Questions: {len(questions)}")
    print(f"Correct Answers: {score}")
    print(f"Wrong Answers: {len(questions) - score}")
    print(f"Final Score: {percentage:.1f}%")

    if percentage >= 80:
        print("Grade: EXCELLENT!")
    elif percentage >= 60:
        print("Grade: VERY GOOD!")
    elif percentage >= 50:
        print("Grade: GOOD!")
    else:
        print("Grade: KEEP PRACTISING!")

    print("===================================")


def main():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Start Quiz")
        print("2. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            start_quiz()
        elif choice == "2":
            print("Thank you for using Mechatronics Quiz App!")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")


if __name__ == "__main__":
    main()
