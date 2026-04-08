import os
import requests

# ===== CONFIG =====
ENV_API_BASE = "https://bhumika45-cyber-defence.hf.space"
MAX_STEPS = 5

# ===== LLM CONFIG (MANDATORY) =====
LLM_BASE_URL = os.environ.get("API_BASE_URL")
LLM_API_KEY = os.environ.get("API_KEY")

# ===== LLM CALL FUNCTION =====
def get_action_from_llm(state):
    try:
        response = requests.post(
            f"{LLM_BASE_URL}/chat/completions",
            headers={
                "Authorization": f"Bearer {LLM_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": "You are a cyber defence agent."},
                    {"role": "user", "content": f"State: {state}. Choose action: safe or attack."}
                ],
                "max_tokens": 10
            },
            timeout=10
        )

        data = response.json()

        # extract response safely
        action_text = data.get("choices", [{}])[0].get("message", {}).get("content", "safe")

        if "attack" in action_text.lower():
            return "attack"
        return "safe"

    except Exception as e:
        print("LLM error:", e)
        return "safe"  # fallback


# ===== ENV FUNCTIONS =====
def reset_env():
    try:
        return requests.post(f"{ENV_API_BASE}/reset", json={"task": "easy"}).json()
    except:
        return {}


def step_env(action):
    try:
        return requests.post(f"{ENV_API_BASE}/step", json={"action": action}).json()
    except:
        return {}


# ===== MAIN =====
def run():
    task_name = "cyber_defence"

    print(f"[START] task={task_name}", flush=True)

    state = reset_env()
    total_reward = 0

    for step in range(1, MAX_STEPS + 1):

        # ✅ CALL LLM (IMPORTANT)
        action = get_action_from_llm(state)

        result = step_env(action)

        reward = 0
        if isinstance(result, dict):
            reward = result.get("reward", 0)

        total_reward += reward

        print(f"[STEP] step={step} reward={reward}", flush=True)

        if isinstance(result, dict) and result.get("done"):
            break

        state = result

    print(f"[END] task={task_name} score={total_reward} steps={step}", flush=True)


if __name__ == "__main__":
    try:
        run()
    except Exception:
        print("[END] task=cyber_defence score=0 steps=0", flush=True)
