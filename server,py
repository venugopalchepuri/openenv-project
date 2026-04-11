from fastapi import FastAPI
from env.environment import GridEnv

app = FastAPI()
env = GridEnv()

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(action: str):
    state, reward, done = env.step(action)
    return {"state": state, "reward": reward, "done": done}

@app.get("/state")
def state():
    return env.state()