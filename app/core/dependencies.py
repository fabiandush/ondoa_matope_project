from app.core.database import SessionLocal
from fastapi import Depends
from fastapi.security import HTTPBearer
from fastapi import HTTPException
from app.core.security import decode_access_token

security = HTTPBearer()

def get_db():
  db = SessionLocal()

  try:
    yield db
  
  finally:
    db.close()



def get_current_member_id(
    credentials = Depends(security)
) -> str:

  try:
    return decode_access_token(
      credentials.credentials
    )

  except Exception:
    raise HTTPException(
      status_code=401,
      detail="Invalid authentication credentials"
    )