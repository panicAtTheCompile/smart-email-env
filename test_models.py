from env.models import Observation

obs = Observation(
    email_text="Hello",
    thread_history=[],
    metadata={"task": "test"}
)

print(obs)