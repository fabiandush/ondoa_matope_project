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
                    full_name,
                    id,
                    name,
                    total_contributed,
                    member_count
                FROM member_scc_stats
                WHERE member_id = :member_id
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
                    id,
                    name,
                    total_contributed,
                    member_count
                FROM member_association_stats
                WHERE member_id = :member_id
            """),
            {
                "member_id": member_id
            }
        )

        return result.mappings().all()