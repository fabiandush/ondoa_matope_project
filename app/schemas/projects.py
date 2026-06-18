from pydantic import BaseModel

class ProjectBase(BaseModel):
  project_name: str
  target_amount: int
  contributed_amount: int