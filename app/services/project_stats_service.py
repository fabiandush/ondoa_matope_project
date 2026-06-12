from app.schemas.projects import ProjectBase
from app.repositories.project_stats_repository import ProjectStatsRepository
from sqlalchemy.orm import Session

def get_project_stats(db: Session) -> list[ProjectBase]:
  return ProjectStatsRepository.get_project_stats(db=db)
