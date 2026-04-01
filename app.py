from fastapi import FastAPI
from env.environment import CyberEnv

app = FastAPI()
env = CyberEnv()

@app.post("/reset")
def reset(task: str):
    return env.reset(task)

@app.post("/step")
def step(action: str):
    return env.step(action)

@app.get("/state")
def state():
    return env.state()