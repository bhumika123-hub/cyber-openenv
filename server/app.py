from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import CyberEnv

# =========================================================
# 🚀 Cyber Defence Environment API
# Exposes reset, step, and state endpoints for agent interaction
# =========================================================

app = FastAPI()

# Initialize environment
env = CyberEnv()


# ===== 📦 REQUEST MODELS =====
class ResetRequest(BaseModel):
    task: str = "easy"   # easy / medium / hard


class StepRequest(BaseModel):
    action: str = "safe"  # safe / attack


# ===== 🏠 ROOT =====
@app.get("/")
def home():
    return {
        "message": "Cyber Defence API is running 🚀",
        "endpoints": ["/reset", "/step", "/state"]
    }


# ===== 🔄 RESET =====
@app.post("/reset")
def reset(req: ResetRequest = None):
    try:
        task = "easy"
        if req and req.task:
            task = req.task

        state = env.reset(task)

        return {
            "task": task,
            "state": state
        }

    except Exception as e:
        return {"error": str(e)}


# ===== ⚙️ STEP =====
@app.post("/step")
def step(req: StepRequest = None):
    try:
        action = "safe"
        if req and req.action:
            action = req.action

        result = env.step(action)

        return result

    except Exception as e:
        return {"error": str(e)}


# ===== 📊 STATE =====
@app.get("/state")
def get_state():
    try:
        return {
            "state": env.state
        }
    except Exception as e:
        return {"error": str(e)}


# ===== 🚀 ENTRY POINT (IMPORTANT FOR VALIDATOR) =====
def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()
