from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import CyberEnv

app = FastAPI()

# Initialize environment (safe)
env = CyberEnv()

# ===== Request Models =====
class ResetRequest(BaseModel):
    task: str = "easy"   # default value

class StepRequest(BaseModel):
    action: str = "safe"  # default value


# ===== Routes =====
@app.get("/")
def home():
    return {"message": "Cyber Defence API is running 🚀"}


@app.post("/reset")
def reset(req: ResetRequest = None):
    try:
        task = "easy"
        if req and req.task:
            task = req.task
        return env.reset(task)
    except Exception as e:
        return {"error": str(e)}


@app.post("/step")
def step(req: StepRequest = None):
    try:
        action = "safe"
        if req and req.action:
            action = req.action
        return env.step(action)
    except Exception as e:
        return {"error": str(e)}


@app.get("/state")
def state():
    try:
        return env.state()
    except Exception as e:
        return {"error": str(e)}


# ===== ENTRY POINT (IMPORTANT) =====
def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
