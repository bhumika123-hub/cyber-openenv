import random

class CyberEnv:
    def __init__(self):
        self.state = {}
        self.step_count = 0
        self.max_steps = 5
        self.task = "easy"

    # ===== RESET =====
    def reset(self, task="easy"):
        self.task = task
        self.step_count = 0

        # 🎯 Difficulty-based initialization
        if task == "easy":
            self.state = {
                "threat_level": random.uniform(0.1, 0.4),
                "traffic_spike": False,
                "failed_logins": random.randint(0, 5),
                "system_health": 0.9
            }

        elif task == "medium":
            self.state = {
                "threat_level": random.uniform(0.4, 0.7),
                "traffic_spike": random.choice([True, False]),
                "failed_logins": random.randint(5, 15),
                "system_health": 0.7
            }

        else:  # hard
            self.state = {
                "threat_level": random.uniform(0.7, 1.0),
                "traffic_spike": True,
                "failed_logins": random.randint(15, 30),
                "system_health": 0.5
            }

        return self.state

    # ===== STEP =====
    def step(self, action):
        self.step_count += 1

        threat = self.state["threat_level"]
        reward = 0

        # 🧠 Reward logic (REALISTIC)
        if action == "attack":
            if threat > 0.6:
                reward = 0.9   # correct response
                self.state["threat_level"] -= 0.3
            else:
                reward = 0.2   # unnecessary attack

        elif action == "safe":
            if threat < 0.4:
                reward = 0.8   # correct safe decision
            else:
                reward = 0.3   # ignored threat

        # 🔄 Dynamic state updates
        self.state["threat_level"] = max(0, min(1, self.state["threat_level"] + random.uniform(-0.1, 0.2)))
        self.state["failed_logins"] += random.randint(0, 3)

        # system health depends on threat
        self.state["system_health"] = max(0, 1 - self.state["threat_level"])

        # introduce anomaly randomly
        self.state["traffic_spike"] = random.choice([True, False])

        done = self.step_count >= self.max_steps

        return {
            "state": self.state,
            "reward": reward,
            "done": done
        }

    # ===== STATE =====
    def state(self):
        return self.state
