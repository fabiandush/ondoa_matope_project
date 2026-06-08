from pydantic import BaseModel, Field

class LookupResponse(BaseModel):
  id: str
  name: str

class SignupLookupsResponse(BaseModel):
  sccs: list[LookupResponse]
  associations: list[LookupResponse]