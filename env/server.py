from fastapi import FastAPI
from env.environment import EmailEnv
from env.models import Action

app = FastAPI()
env = EmailEnv()


@app.post("/reset")
async def reset():
    result = await env.reset()

    return {
        "observation": {
            "email_text": result.observation.email_text,
            "thread_history": result.observation.thread_history,
            "metadata": result.observation.metadata,
        },
        "reward": float(result.reward),
        "done": bool(result.done),
        "info": {}
    }


@app.post("/step")
async def step(action: dict):
    act = Action(**action)
    result = await env.step(act)

    return {
        "observation": {
            "email_text": result.observation.email_text,
            "thread_history": result.observation.thread_history,
            "metadata": result.observation.metadata,
        },
        "reward": float(result.reward),
        "done": bool(result.done),
        "info": {}
    }


@app.get("/state")
async def state():
    return await env.state()