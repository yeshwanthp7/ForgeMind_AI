def recommend(root_cause, risk_level):
    if "Cooling" in root_cause:
        return [
            "Inspect the cooling fan.",
            "Check coolant level.",
            "Reduce machine load.",
            "Stop the machine if temperature exceeds safety limits."
        ]

    elif "bearing" in root_cause.lower():
        return [
            "Inspect bearings.",
            "Lubricate moving parts.",
            "Replace damaged bearing."
        ]

    elif risk_level == "CRITICAL":
        return [
            "Stop machine immediately.",
            "Notify maintenance team.",
            "Perform complete inspection."
        ]

    else:
        return [
            "Continue monitoring machine.",
            "Schedule preventive maintenance."
        ]


root_cause = "Cooling system malfunction"
risk = "CRITICAL"

actions = recommend(root_cause, risk)

print("\nRecommended Actions:\n")

for i, action in enumerate(actions, 1):
    print(f"{i}. {action}")