# Rule-Based Expert System

## Project Description

This project implements a Rule-Based Expert System using the Forward Chaining inference technique.

The system accepts user symptoms as facts, applies IF-THEN rules, and derives conclusions step by step.

---

## AI Technique Used

Forward Chaining

The system starts from known facts and repeatedly applies rules until no new facts can be inferred.

---

## Features

- Rule Engine
- Knowledge Base
- User Input
- Forward Chaining
- Multi-step Inference
- Reasoning Log
- Console Interface

---

## Project Structure

```text
Rule_Based_Expert_System

│
├── main.py
├── README.md
└── requirements.txt
```

---

## Example Rules

Rule 1

IF fever AND cough

THEN flu

Rule 2

IF flu

THEN visit_doctor

Rule 3

IF visit_doctor

THEN take_medicine

---

## Sample Execution

Input

```text
fever,cough
```

Output

```text
Initial Facts

fever
cough

Inference Steps

Step 1
IF cough, fever
THEN flu

Step 2
IF flu
THEN visit_doctor

Step 3
IF visit_doctor
THEN take_medicine

Final Conclusions

cough
fever
flu
visit_doctor
take_medicine
```

---

## Technologies Used

- Python
- Rule-Based AI
- Forward Chaining

---

## Author

Manan
