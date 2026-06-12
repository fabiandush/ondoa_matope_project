from pydantic import BaseModel

class ProjectBase(BaseModel):
  name: str
  target_amount: int
  default_pledge_amount: int