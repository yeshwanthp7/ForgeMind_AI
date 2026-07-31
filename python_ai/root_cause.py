def find_root_cause(incident):
    """
    Predict the possible root cause based on the incident description.
    """

    incident = incident.lower()

    if "temperature" in incident or "overheating" in incident:
        return "Cooling system malfunction"

    elif "pressure" in incident:
        return "Pressure valve failure"

    elif "gas" in incident or "leak" in incident:
        return "Gas pipeline leakage"

    elif "vibration" in incident:
        return "Bearing wear or motor imbalance"

    else:
        return "Root cause not identified"


# Test
if __name__ == "__main__":
    incident = "Machine temperature is increasing and overheating."

    cause = find_root_cause(incident)

    print("Incident:")
    print(incident)

    print("\nPredicted Root Cause:")
    print(cause)

def find_root_cause(risk_level, incident_text):
    text = incident_text.lower()

    if "cooling" in text or "overheat" in text:
        return "Cooling system failure caused overheating."

    elif "pressure" in text:
        return "Abnormal pressure detected. Possible valve blockage."

    elif "vibration" in text:
        return "High vibration indicates possible bearing failure."

    elif "temperature" in text:
        return "Excessive temperature detected. Cooling efficiency reduced."

    else:
        if risk_level == "CRITICAL":
            return "Multiple failures detected. Immediate inspection required."
        elif risk_level == "HIGH":
            return "Potential equipment malfunction."
        else:
            return "No major root cause identified."