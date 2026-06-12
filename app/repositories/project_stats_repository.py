from sqlalchemy import text
from sqlalchemy.orm import Session

class ProjectStatsRepository:
  @staticmethod
  def get_project_stats(db: Session) -> dict:
    result = db.execute(
      text("""
           select name, target_amount, default_pledge_amount
           from projects
           """)

    )
    return result.mappings().all()