import requests

API_BASE_URL = "https://bhumika45-cyber-defence.hf.space"
MAX_STEPS = 5


def reset_env():
    try:
        res = requests.post(f"{API_BASE_URL}/reset", json={"task": "easy"})
        return res.json()
    except:
        return {}


def step_env(action):
    try:
        res = requests.post(f"{API_BASE_URL}/step", json={"action": action})
        return res.json()
    except:
        return {}


def run():
    task_name = "cyber_defence"

    # ✅ START BLOCK
    print(f"[START] task={task_name}", flush=True)

    state = reset_env()

    total_reward = 0

    for step in range(1, MAX_STEPS + 1):
        action = "safe"  # fallback action

        result = step_env(action)

        reward = 0
        if isinstance(result, dict):
            reward = result.get("reward", 0)

        total_reward += reward

        # ✅ STEP BLOCK
        print(f"[STEP] step={step} reward={reward}", flush=True)

        if isinstance(result, dict) and result.get("done"):
            break

    # ✅ END BLOCK
    print(
        f"[END] task={task_name} score={total_reward} steps={step}",
        flush=True
    )


if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(f"[END] task=cyber_defence score=0 steps=0", flush=True)
