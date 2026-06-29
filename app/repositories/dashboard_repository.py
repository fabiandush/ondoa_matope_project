from sqlalchemy import text
from sqlalchemy.orm import Session


class DashboardRepository:

    @staticmethod
    def get_project(
        db: Session,
    ):
        result = db.execute(
            text("""
                SELECT
                    project_name,
                    target_amount,
                    contributed_amount
                FROM project_stats
                LIMIT 1
            """)
        )

        return result.mappings().one()

    @staticmethod
    def get_contribution(
        db: Session,
        member_id: str,
    ):
        result = db.execute(
            text("""
                SELECT
                    pledge_amount,
                    contributed_amount
                FROM member_contribution_stats
                WHERE member_id = :member_id
            """),
            {
                "member_id": member_id
            }
        )

        return result.mappings().one()

    @staticmethod
    def get_scc(
        db: Session,
        member_id: str,
    ):
        result = db.execute(
            text("""
                SELECT
                    s.id,
                    s.name,
                    s.total_contributed,
                    s.member_count
                FROM members m
                Join scc_contribution_stats s
                  ON s.id = m.scc_id
                WHERE m.id = :member_id
            """),
            {
                "member_id": member_id
            }
        )

        return result.mappings().one()

    @staticmethod
    def get_associations(
        db: Session,
        member_id: str,
    ):
        result = db.execute(
            text("""
                SELECT
                  a.id,
                  a.name,
                  a.total_contributed,
                  a.member_count
                FROM member_associations ma
                JOIN association_contribution_stats a
                  ON a.id = ma.association_id
                WHERE ma.member_id = :member_id
            """),
            {
                "member_id": member_id
            }
        )

        return result.mappings().all()