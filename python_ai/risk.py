def calculate_risk(data):

    score = 0

    # Temperature check
    if data["temperature"] > 90:
        score += 40

    # Pressure check
    if data["pressure"] > 150:
        score += 30

    # Vibration check
    if data["vibration"] > 8:
        score += 30


    # Risk level calculation
    if score >= 80:
        level = "CRITICAL"

    elif score >= 50:
        level = "HIGH"

    elif score >= 20:
        level = "MEDIUM"

    else:
        level = "LOW"


    return score, level


# Test data (optional)
if __name__ == "__main__":

    machine_data = {
        "temperature": 120,
        "pressure": 160,
        "vibration": 9
    }

    score, level = calculate_risk(machine_data)

    print("Risk Score:", score)
    print("Risk Level:", level)