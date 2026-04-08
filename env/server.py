from fastapi import FastAPI
from env.environment import EmailEnv
from env.models import Action

app = FastAPI()

env = EmailEnv()


@app.post("/reset")
async def reset():
    result = await env.reset()
    return {
        "observation": result.observation.dict(),
        "reward": result.reward,
        "done": result.done
    }


@app.post("/step")
async def step(action: dict):
    act = Action(**action)
    result = await env.step(act)

    return {
        "observation": result.observation.dict(),
        "reward": result.reward,
        "done": result.done
    }


@app.get("/state")
async def state():
    return await env.state()