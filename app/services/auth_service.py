from app.core.security import create_access_token, verify_password
from sqlalchemy.orm import Session
from app.core.exceptions import PhoneAlreadyExistsException, UserDoesNotExist, InvalidCredentialsException

from app.repositories.member_repository import MemberRepository
from app.repositories.reconcilitation_repository import ReconciliationRepository
from app.schemas.auth import AuthResponse, MemberSummary
from app.utils.phone import normalize_phone, get_phone_parts


from app.core.security import (
  hash_password
)

## Signing up a new user
def register_user(
    db: Session,
    full_name: str,
    phone: str,
    password: str,
    scc_id: str | None,
    association_ids: list[str]
) -> AuthResponse: 
  
  phone = normalize_phone(phone)

  ## Check if user with the same phone already exists
  existing = MemberRepository.get_by_phone(
    db=db,
    phone=phone
  )

  if existing:
    raise PhoneAlreadyExistsException()

  ## Hash password
  hashed_password = hash_password(password)


  phone_front, phone_back = get_phone_parts(phone)

  try:

    member = MemberRepository.create_member(
      db=db,
      full_name=full_name,
      phone=phone,
      password_hash=hashed_password,
      scc_id=scc_id
    )

    MemberRepository.add_associations(
      db=db,
      member_id = member["id"],
      association_ids = association_ids
    )
    MemberRepository.create_phone(
      db=db,
      member_id=member["id"],
      phone=phone,
      phone_front=phone_front,
      phone_back=phone_back,
    )

    ReconciliationRepository.claim_member_transactions(
      db=db,
      member_id = member["id"],
    )

    db.commit()
  except Exception:
    db.rollback()
    raise

  return AuthResponse(
    token=create_access_token(
      str(member["id"])
    ),
    member = MemberSummary(
      id=str(member["id"]),
      full_name = member["full_name"],
      role=member["role"],
      scc_id = str(member["scc_id"])
    )
  )

## Sign in User
def login_user(
    db: Session,
    phone: str,
    password: str
) -> AuthResponse:
  
  phone = normalize_phone(phone)

  member = MemberRepository.get_by_phone_for_auth(
    db=db,
    phone=phone
  )

  if not member:
    raise UserDoesNotExist()
  
  if not verify_password(
    password,
    member["password_hash"]
  ): 
    raise InvalidCredentialsException()
  
  ReconciliationRepository.claim_member_transactions(
    db = db,
    member_id=member["id"],
  )
  
  return AuthResponse(
    token = create_access_token(
      str(member["id"])
    ),
    member = MemberSummary(
      id=str(member["id"]),
      full_name=member["full_name"],
      role=member["role"],
      scc_id=str(member["scc_id"]) if member["scc_id"] else None
    )
  )