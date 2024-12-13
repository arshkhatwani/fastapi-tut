from fastapi import APIRouter, Depends
from schemas import UserBase, UserDisplay
from typing import List
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user


router = APIRouter(prefix='/users', tags=['users'])


@router.post('/', response_model=UserDisplay)
def add_user(request: UserBase, db_session: Session = Depends(get_db)):
    user = db_user.create_user(db_session, request)
    return user


@router.get('/all', response_model=List[UserDisplay])
def get_all_users(db_session: Session = Depends(get_db)):
    users = db_user.get_users(db_session)
    return users


@router.get('/{id}', response_model=UserDisplay | None)
def get_single_user(id: int, db_session: Session = Depends(get_db)):
    return db_user.get_user_by_id(db_session, id)


@router.put('/{id}')
def update_user(id: int, request: UserBase, db_session: Session = Depends(get_db)):
    return db_user.update_user(db_session, id, request)


@router.delete('/{id}')
def delete_user(id: int, db_session: Session = Depends(get_db)):
    return db_user.delete_user(db_session, id)
