from sqlalchemy import text
from sqlalchemy.orm import Session
class MemberRepository:

  @staticmethod
  def get_by_phone(
    db: Session,
    phone: str
  ):
    result = db.execute(
    text("""
         select * from members
         where phone = :phone
         limit 1
      """),
         {"phone": phone}
    )
    return result.mappings().first()
  
  @staticmethod
  def add_associations(
      db: Session,
      member_id: str,
      association_ids: list[str]
  ):
      if not association_ids:
          return

      db.execute(
          text("""
              insert into member_associations (
                  member_id,
                  association_id
              )
              values (
                  :member_id,
                  :association_id
              )
          """),
          [
              {
                  "member_id": member_id,
                  "association_id": association_id
              }
              for association_id in association_ids
          ]
      )

  @staticmethod
  def create_member(
    db: Session,
    full_name: str,
    phone: str,
    password_hash: str,
    scc_id: str | None
  ):
    result = db.execute(
    text("""
         insert into members (
         full_name,
         phone,
         password_hash,
         scc_id
         )
         values (
         :full_name,
         :phone,
         :password_hash,
         :scc_id
         )
         returning id
         """),
         {
           "full_name": full_name,
           "phone": phone,
           "password_hash": password_hash,
           "scc_id": scc_id
         }
    )
    member_id = result.scalar()

    return member_id
  

  