from pydantic import BaseModel, Field
from uuid import UUID

class LookupResponse(BaseModel):
  id: UUID
  name: str

class SignupLookupsResponse(BaseModel):
  sccs: list[LookupResponse]
  associations: list[LookupResponse]