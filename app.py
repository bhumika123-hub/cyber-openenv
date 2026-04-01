from fastapi import FastAPI
from pydantic import BaseModel
from env.environment import CyberEnv

app = FastAPI()
env = CyberEnv()

class ResetRequest(BaseModel):
    task: str

class StepRequest(BaseModel):
    action: str

@app.get("/")
def home():
    return {"message": "Cyber Defence API is running 🚀"}

@app.post("/reset")
def reset(req: ResetRequest):
    return env.reset(req.task)

@app.post("/step")
def step(req: StepRequest):
    return env.step(req.action)

@app.get("/state")
def state():
    return env.state()
