from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.dependencies import get_db

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://ondoa-matope.fabianndush.workers.dev/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


## Register Router
from app.api.auth import router as auth_router
from app.api.lookup import router as lookup_router
from app.api.dashboard import router as dashboard_router


app.include_router(auth_router)
app.include_router(lookup_router)
app.include_router(dashboard_router)


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