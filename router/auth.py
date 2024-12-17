from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.database import get_db
from db.db_user import DbUser
from db.hash import Hash
from auth.oauth2 import create_access_token

router = APIRouter(
    tags=['auth']
)


@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.name == request.username).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'User not found')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Invalid credentials')

    access_token = create_access_token(data={'sub': user.name})

    return {
        'access_token': access_token,
        'token_type': 'bearer',
        'username': user.name,
        'user_id': user.id
    }
