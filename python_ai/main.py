from risk import calculate_risk
from root_cause import find_root_cause
from recommendation import recommend


def analyze_incident(machine_data):

    # Risk calculation
    score, level = calculate_risk(machine_data)

    # Root cause
    incident = "Machine temperature is increasing and overheating"

    cause = find_root_cause(level, incident)

    # Recommendation
    actions = recommend(cause, level)

    return {
        "risk_score": score,
        "risk_level": level,
        "root_cause": cause,
        "recommendations": actions
    }


# Run directly for testing
if __name__ == "__main__":

    machine_data = {
        "temperature": 120,
        "pressure": 160,
        "vibration": 9
    }

    result = analyze_incident(machine_data)

    print(result)