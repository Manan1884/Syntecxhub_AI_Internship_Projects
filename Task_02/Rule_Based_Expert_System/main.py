rules = [

    {
        "conditions": {"fever", "cough"},
        "conclusion": "flu"
    },

    {
        "conditions": {"flu"},
        "conclusion": "visit_doctor"
    },

    {
        "conditions": {"visit_doctor"},
        "conclusion": "take_medicine"
    },

    {
        "conditions": {"fever", "rash"},
        "conclusion": "measles"
    },

    {
        "conditions": {"measles"},
        "conclusion": "isolate_patient"
    },

    {
        "conditions": {"sore_throat", "fever"},
        "conclusion": "throat_infection"
    },

    {
        "conditions": {"throat_infection"},
        "conclusion": "drink_warm_water"
    }

]

def forward_chaining(facts):

    inferred = set(facts)

    reasoning_log = []

    changed = True

    while changed:

        changed = False

        for rule in rules:

            conditions = rule["conditions"]
            conclusion = rule["conclusion"]

            if conditions.issubset(inferred):

                if conclusion not in inferred:

                    inferred.add(conclusion)

                    changed = True

                    reasoning_log.append(
                        {
                            "conditions": conditions,
                            "conclusion": conclusion
                        }
                    )

    return inferred, reasoning_log

print("=" * 55)
print("        RULE-BASED EXPERT SYSTEM")
print("=" * 55)

print("\nAvailable Symptoms:")

print("""
fever
cough
rash
sore_throat
""")

user_input = input(
    "\nEnter symptoms (comma separated): "
)

facts = set()

for symptom in user_input.split(","):

    symptom = symptom.strip().lower()

    if symptom:

        facts.add(symptom)


print("\nInitial Facts:")

for fact in sorted(facts):

    print("-", fact)


final_facts, log = forward_chaining(facts)


print("\n" + "=" * 55)
print("Inference Steps")
print("=" * 55)

if log:

    for step_number, step in enumerate(log, start=1):

        conditions = ", ".join(sorted(step["conditions"]))

        conclusion = step["conclusion"]

        print(f"\nStep {step_number}")

        print(f"IF {conditions}")

        print(f"THEN {conclusion}")

else:

    print("No rules were triggered.")


print("\n" + "=" * 55)
print("Final Conclusions")
print("=" * 55)

for fact in sorted(final_facts):

    print("-", fact)