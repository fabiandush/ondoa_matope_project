from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.services.groups import get_sccs, get_associations, get_signup_lookups
from app.schemas.groups import LookupResponse, SignupLookupsResponse
from app.schemas.projects import ProjectBase
from app.services.project_stats_service import get_project_stats 

router = APIRouter(
    prefix="/lookups",
    tags=["Lookups"]
)


@router.get(
    "/sccs",
    response_model=LookupResponse,
    status_code = status.HTTP_200_OK
)
def get_sccs_endpoint(
    db: Session = Depends(get_db)
):
    return get_sccs(db=db)



@router.get(
    "/associations",
    response_model = LookupResponse,
    status_code = status.HTTP_200_OK
)
def get_associations_endpoint(
    db: Session = Depends(get_db)
):
    return get_associations(request=None, db=db)

@router.get(
    "/project-stats",
    response_model = list[ProjectBase],
    status_code = status.HTTP_200_OK
)
def get_project_stats_endpoint(
    db: Session = Depends(get_db)
):
    return get_project_stats(db=db)

@router.get(
    "/signup-options",
    response_model = SignupLookupsResponse,
    status_code = status.HTTP_200_OK
)
def get_signup_options(
    db: Session = Depends(get_db)
):
    return get_signup_lookups(db=db)