from pydantic import BaseModel
from typing import List, Dict, Optional

class Observation(BaseModel):
    email_text: str
    thread_history: List[str]
    metadata: Dict

class Action(BaseModel):
    action_type: str  # classify | extract | respond
    content: str

class StepResult(BaseModel):
    observation: Observation
    reward: float
    done: bool
    info: Optional[Dict] = None