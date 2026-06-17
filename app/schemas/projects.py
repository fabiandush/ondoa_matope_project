from pydantic import BaseModel

class ProjectBase(BaseModel):
  name: str
  target_amount: int
  contributed_amount: int