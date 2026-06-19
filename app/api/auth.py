from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth import SignUpRequest, LoginRequest
from app.services.auth_service import register_user, login_user
from app.core.dependencies import get_db
from app.schemas.auth import AuthResponse
from app.core.exceptions import PhoneAlreadyExistsException

router = APIRouter(
  prefix="/auth",
  tags=["Authentication"]
)

@router.post(
    "/signup",
    response_model = AuthResponse,
    status_code = status.HTTP_201_CREATED
)
def signup_endpoint(
  request: SignUpRequest,
  db: Session = Depends(get_db)
): 

  return register_user(
    db=db,
    full_name=request.full_name,
    phone=request.phone,
    password=request.password,
    scc_id=request.scc_id,
    association_ids=request.association_ids
  )

@router.post(
  "/login",
  response_model=AuthResponse,
  status_code=status.HTTP_200_OK
)
def login_endpoint(
  request: LoginRequest,
  db: Session = Depends(get_db)
):
  return login_user(
    db=db,
    phonr=request.phone,
    password=request.password
  )