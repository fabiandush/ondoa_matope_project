from app.core.security import create_access_token
from sqlalchemy.orm import Session
from app.core.exceptions import PhoneAlreadyExistsException

from app.repositories.member_repository import MemberRepository
from app.schemas.auth import AuthResponse

from app.core.security import (
  hash_password
)

## Signing up a new user
def register_user(
    db: Session,
    full_name: str,
    phone: str,
    password: str,
    scc_id: str | None
) -> AuthResponse: 
  
  ## Check if user with the same phone already exists
  existing = MemberRepository.get_by_phone(
    db=db,
    phone=phone
  )

  if existing:
    raise PhoneAlreadyExistsException()

  ## Hash password
  hashed_password = hash_password(password)


  member_id = MemberRepository.create_member(
    db=db,
    full_name=full_name,
    phone=phone,
    password_hash=hashed_password,
    scc_id=scc_id
  )

  return AuthResponse(
    member_id=member_id,
    token=create_access_token(
      str(member_id)
    )
  )