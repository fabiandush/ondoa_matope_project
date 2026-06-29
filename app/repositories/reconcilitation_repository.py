from sqlalchemy import text
from sqlalchemy.orm import Session

class ReconciliationRepository:
  @staticmethod
  def claim_member_transactions(
    db: Session,
    member_id: str,
  ) -> int:
    result = db.execute(
      text("""
          SELECT public.claim_member_transactions(
           :member_id
           ),
           """),
          {
          "member_id": member_id
          }
    )
    return result.scalar_one()