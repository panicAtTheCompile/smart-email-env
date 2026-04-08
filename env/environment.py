import random
from env.models import Observation, StepResult
from env.tasks import TASKS


class EmailEnv:

    def __init__(self):
        self.current_task = None
        self.done = False
        self.stage = 0

    async def reset(self):
        self.current_task = random.choice(TASKS)
        self.done = False
        self.stage = 0

        return StepResult(
            observation=Observation(
                email_text=self.current_task["email"],
                thread_history=[],
                metadata={
                    "task": self.current_task["name"],
                    "stage": self.stage
                }
            ),
            reward=0.0,
            done=False
        )

    async def step(self, action):
        reward = 0.0

        # Stage 0: classification
        if self.stage == 0:
            if "normal" in action.content.lower():
                reward = 1.0
            else:
                reward = 0.0
            self.stage += 1
            done = False

        # Stage 1: extraction
        elif self.stage == 1:
            score = 0.0
            if "5th april" in action.content.lower():
                score += 0.5
            if "high" in action.content.lower():
                score += 0.5
            reward = score
            self.stage += 1
            done = False

        # Stage 2: response
        else:
            score = 0.0
            if "sorry" in action.content.lower():
                score += 0.5
            if "refund" in action.content.lower():
                score += 0.5
            reward = score
            done = True

        return StepResult(
            observation=Observation(
                email_text=self.current_task["email"],
                thread_history=[],
                metadata={
                    "task": self.current_task["name"],
                    "stage": self.stage
                }
            ),
            reward=reward,
            done=done
        )

    async def state(self):
        return {
            "task": self.current_task,
            "stage": self.stage
        }

    async def close(self):
        pass