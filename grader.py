def grade_easy(action):
    return 1.0 if action == "block" else 0.0


def grade_medium(action):
    return 1.0 if action == "phishing" else 0.5


def grade_hard(actions):
    if "stop_attack" in actions:
        return 1.0
    elif "detect_stage" in actions:
        return 0.5
    return 0.0