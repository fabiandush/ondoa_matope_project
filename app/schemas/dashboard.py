from pydantic import BaseModel

class DashboardProject(BaseModel):
  project_name: str
  target_amount: int
  raised_amount: int

class DashboardContribution(BaseModel):
  pledge_amount: int
  contributed_amount: int

class DashboardCommunity(BaseModel):
  id: str
  name: str
  total_contributed: int
  member_count: int

class DashboardResponse(BaseModel):
  project: DashboardProject
  contribution: DashboardContribution
  scc: DashboardCommunity
  associations: list[DashboardCommunity]