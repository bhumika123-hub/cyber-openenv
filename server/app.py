from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional
from env.environment import CyberEnv

app = FastAPI()

# Initialize environment
env = CyberEnv()


# ================= REQUEST MODELS =================
class ResetRequest(BaseModel):
    task: Optional[str] = None


class StepRequest(BaseModel):
    action: Optional[str] = None


# ================= ROOT =================
@app.get("/")
def home():
    return {"message": "Cyber Defence API is running 🚀"}


# ================= RESET =================
@app.post("/reset")
def reset(req: ResetRequest = Body(None), task: str = None):
    """
    Supports:
    - JSON body: {"task": "easy"}
    - Query: /reset?task=easy
    - Empty: defaults to "easy"
    """
    task_name = req.task if req and req.task else task or "easy"
    return env.reset(task_name)


# ================= STEP =================
@app.post("/step")
def step(req: StepRequest = Body(None), action: str = None):
    """
    Supports:
    - JSON body: {"action": "block"}
    - Query: /step?action=block
    - Empty: defaults to "noop"
    """
    act = req.action if req and req.action else action or "noop"
    return env.step(act)


# ================= STATE =================
@app.get("/state")
def state():
    return env.state()
