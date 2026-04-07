import os
import requests

# ================= CONFIG =================
API_BASE_URL = "https://bhumika45-cyber-defence.hf.space"
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

MAX_STEPS = 5

print("Inference file loaded successfully")

# ================= HELPER FUNCTIONS =================
def reset_env():
    try:
        res = requests.post(f"{API_BASE_URL}/reset", json={"task": "easy"})
        return res.json()
    except Exception as e:
        print("Reset error:", e)
        return {}

def step_env(action):
    try:
        res = requests.post(f"{API_BASE_URL}/step", json={"action": action})
        return res.json()
    except Exception as e:
        print("Step error:", e)
        return {}

def get_state():
    try:
        res = requests.get(f"{API_BASE_URL}/state")
        return res.json()
    except Exception as e:
        print("State error:", e)
        return {}

# ================= MAIN LOGIC =================
def run_inference():
    print("Starting inference...")

    state = reset_env()
    print("Initial State:", state)

    for i in range(MAX_STEPS):
        print(f"\nStep {i+1}")

        # Fallback safe action (no API key needed)
        action = "safe"

        result = step_env(action)
        print("Result:", result)

        if isinstance(result, dict) and result.get("done"):
            print("Task completed early")
            break

    final_state = get_state()
    print("\nFinal State:", final_state)

    print("Inference completed successfully")

# ================= ENTRY POINT =================
if __name__ == "__main__":
    try:
        run_inference()
    except Exception as e:
        print("FATAL ERROR:", str(e))
