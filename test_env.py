import asyncio
from env.environment import EmailEnv
from env.models import Action

async def test():
    env = EmailEnv()

    res = await env.reset()
    print("RESET:", res)

    action = Action(action_type="respond", content="Sorry, refund processed")
    res = await env.step(action)
    print("STEP:", res)

asyncio.run(test())
