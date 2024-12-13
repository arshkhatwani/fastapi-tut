from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser
from db.hash import Hash


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        name=request.name,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_users(db: Session):
    users = db.query(DbUser).all()
    return users


def get_user_by_id(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    return user
