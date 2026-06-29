from datetime import datetime, timedelta, UTC
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings

pwd_context = CryptContext(
  schemes = ["bcrypt"],
  deprecated = "auto",
)


def hash_password(password: str) -> str:
  return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
  return pwd_context.verify(
    plain_password,
    hashed_password
  )

def create_access_token(
    subject: str
) -> str:
  
  expire = datetime.now(UTC) + timedelta(
    minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES
  )

  payload = {
    "sub": subject,
    "iat": datetime.now(UTC),
    "exp": expire
  }

  return jwt.encode(
    payload,
    settings.JWT_SECRET_KEY,
    algorithm = settings.JWT_ALGORITHM
  )

def decode_access_token(
    token: str
) -> str:
  try:
    payload = jwt.decode(
      token,
      settings.JWT_SECRET_KEY,
      algorithms=[settings.JWT_ALGORITHM]
    )

    member_id = payload.get("sub")

    if not member_id:
      raise ValueError("Token Missing Subject")
    
    return member_id
  
  except JWTError:
    raise ValueError("Invalid Token")