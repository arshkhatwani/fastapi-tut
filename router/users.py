from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db.db_user import create_user


router = APIRouter(prefix='/users', tags=['users'])


@router.post('/', response_model=UserDisplay)
def add_user(request: UserBase, db_session: Session = Depends(get_db)):
    user = create_user(db_session, request)
    return user
