class CyberEnv:
    def __init__(self):
        self.state_data = {}
        self.current_task = None

    def reset(self, task="easy"):
        self.current_task = task
        self.state_data = {
            "failed_logins": 0,
            "email_flag": None,
            "attack_stage": 0
        }
        return self.state()

    def state(self):
        return self.state_data

    def step(self, action):
        reward = 0.0
        done = False

        if self.current_task == "easy":
            if action == "block":
                reward = 1.0
            else:
                reward = -1.0
            done = True

        elif self.current_task == "medium":
            if action == "phishing":
                reward = 1.0
            else:
                reward = -0.5
            done = True

        elif self.current_task == "hard":
            if action == "detect_stage":
                reward = 0.3
            elif action == "stop_attack":
                reward = 1.0
                done = True
            else:
                reward = -1.0

        return self.state(), reward, done, {}