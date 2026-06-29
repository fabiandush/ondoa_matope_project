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
         select id, full_name, phone, role, scc_id from members
         where phone = :phone
         limit 1
      """),
         {"phone": phone}
    )
    return result.mappings().first()
  
  @staticmethod
  def get_by_phone_for_auth(
     db:Session,
     phone: str
  ):
     result = db.execute(
        text("""
              SELECT id, full_name, phone, role, scc_id, password_hash
              FROM members
              WHERE phone = :phone
              LIMIT 1
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
         returning 
          id,
          full_name,
          role,
          scc_id
         """),
         {
           "full_name": full_name,
           "phone": phone,
           "password_hash": password_hash,
           "scc_id": scc_id
         }
    )

    return result.mappings().one()
  
@staticmethod
def create_phone(
    db: Session,
    member_id: str,
    phone: str,
    phone_front: str,
    phone_back: str,
    is_primary: bool = True,
) -> None:

    db.execute(
        text("""
            INSERT INTO member_phones (
                member_id,
                phone,
                phone_front,
                phone_back,
                is_primary
            )
            VALUES (
                :member_id,
                :phone,
                :phone_front,
                :phone_back,
                :is_primary
            )
        """),
        {
            "member_id": member_id,
            "phone": phone,
            "phone_front": phone_front,
            "phone_back": phone_back,
            "is_primary": is_primary,
        },
    )
  