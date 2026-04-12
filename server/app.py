# ===== FIX PYTHON PATH (IMPORTANT FOR DOCKER) =====
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ===== IMPORTS =====
from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import CyberEnv

# =========================================================
# 🚀 Cyber Defence Environment API
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
        task = req.task if req and req.task else "easy"

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
        action = req.action if req and req.action else "safe"

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


# ===== 🚀 ENTRY POINT =====
def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()
