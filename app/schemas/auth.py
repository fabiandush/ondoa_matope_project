from pydantic import BaseModel, Field

class SignUpRequest(BaseModel):
  full_name: str = Field(
    description = "User's full name",
    min_length = 3,
    max_length = 100
  )
  phone: str = Field(
    description = "User's phone number used for login",
    pattern = r"^(?:254|\+254|0)?[71]\d{8}$"
  )
  password: str = Field(
    description = "User password",
    min_length = 6,
    max_length = 128
  )
  scc_id: str | None = Field(
    default = None,
    description = "Small Christian Community Identifier"
  )
  association_ids: list[str] = Field(default_factory=list)

class LoginRequest(BaseModel):
  phone: str = Field(
    pattern = r"^(?:254|\+254|0)?[71]\d{8}$"
  )
  password: str

class AuthResponse(BaseModel):
  member: MemberSummary
  token: str

class MemberSummary(BaseModel):
  id: str
  full_name: str
  role: str
  scc_id: str | None