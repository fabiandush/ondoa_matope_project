from sqlalchemy import text
from sqlalchemy.orm import Session


class GroupRepository:
  @staticmethod
  def get_sccs(db: Session) -> list[dict]:
    result = db.execute(
        text("""
            select
                id,
                name
            from sccs
            order by name
        """)
    )

    return result.mappings().all()
  
  @staticmethod
  def get_associations(db: Session) -> list[dict]:
    result = db.execute(
        text("""
            select
                id,
                name
            from associations
            where is_active = true
            order by name
        """)
    )

    return result.mappings().all()