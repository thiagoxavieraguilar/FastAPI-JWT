from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.depends import get_db_session
from app.auth import UserCase
from app.schemas import User
router = APIRouter(prefix='/user')

@router.post('/register')
def register(user: User, db_session: Session = Depends(get_db_session)):
    uc = UserCase(db_session=db_session)
    uc.user_register(user=user)
    
    return JSONResponse(
        content={'msg': 'success'},
        status_code=status.HTTP_201_CREATED
    )
