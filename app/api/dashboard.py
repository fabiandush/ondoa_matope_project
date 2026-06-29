from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import (
    get_db,
    get_current_member_id,
)

from app.schemas.dashboard import DashboardResponse

from app.services.dashboard_service import get_dashboard

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "",
    response_model=DashboardResponse,
)
def dashboard(
    member_id: str = Depends(get_current_member_id),
    db: Session = Depends(get_db),
):
    return get_dashboard(
        db=db,
        member_id=member_id,
    )