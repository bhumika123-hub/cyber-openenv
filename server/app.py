import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# Try importing environment safely
try:
    from env.environment import CyberEnv
    env = CyberEnv()
except Exception as e:
    print("Environment initialization error:", e)
    env = None

app = FastAPI()

# ===== Request Models =====
class ResetRequest(BaseModel):
    task: str = "easy"

class StepRequest(BaseModel):
    action: str = "safe"


# ===== Routes =====
@app.get("/")
def home():
    return {"message": "Cyber Defence API is running 🚀"}


@app.post("/reset")
def reset(req: ResetRequest = None):
    try:
        if env is None:
            return {"error": "Environment not initialized"}

        task = req.task if req and req.task else "easy"
        return env.reset(task)

    except Exception as e:
        return {"error": str(e)}


@app.post("/step")
def step(req: StepRequest = None):
    try:
        if env is None:
            return {"error": "Environment not initialized"}

        action = req.action if req and req.action else "safe"
        return env.step(action)

    except Exception as e:
        return {"error": str(e)}


@app.get("/state")
def state():
    try:
        if env is None:
            return {"error": "Environment not initialized"}

        return env.state()

    except Exception as e:
        return {"error": str(e)}


# ===== ENTRY POINT (REQUIRED FOR OPENENV) =====
def main():
    print("Starting Cyber Defence API...")
    uvicorn.run(app, host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()
