from app.schemas.groups import LookupResponse, SignupLookupsResponse
from app.repositories.group_repository import GroupRepository

from sqlalchemy.orm import Session

def get_sccs(db: Session) -> list[LookupResponse]:
  return GroupRepository.get_scc(db)


def get_associations(db: Session) -> list[LookupResponse]:
  return GroupRepository.get_associations(db)

def get_signup_lookups(
    db: Session
) -> SignupLookupsResponse:
  return SignupLookupsResponse(
    sccs = get_sccs(db=db),
    associations = get_associations(db=db)
  )


