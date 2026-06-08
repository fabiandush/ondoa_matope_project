from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.dependencies import get_db

app = FastAPI()


## Register Router
from app.api.auth import router as auth_router

app.include_router(auth_router)


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/db-health")
def db_health(
    db: Session = Depends(get_db)
):
    result = db.execute(
        text("select now()")
    )

    return {
        "database_time": str(result.scalar())
    }