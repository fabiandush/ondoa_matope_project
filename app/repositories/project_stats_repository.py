from sqlalchemy import text
from sqlalchemy.orm import Session

class ProjectStatsRepository:
  @staticmethod
  def get_project_stats(db: Session) -> dict:
    result = db.execute(
      text("""
           select project_name, target_amount, contributed_amount
           from project_stats
           LIMIT 1
           """)

    )
    return result.mappings().first()