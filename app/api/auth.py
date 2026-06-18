from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth import SignUpRequest
from app.services.auth_service import register_user
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
  try:

    return register_user(
      db=db,
      full_name=request.full_name,
      phone=request.phone,
      password=request.password,
      scc_id=request.scc_id,
      association_ids=request.association_ids
    )
  
  except PhoneAlreadyExistsException:
    raise HTTPException(
      status_code = status.HTTP_409_CONFLICT,
      detail = "A user with this phone number already exists."
    )