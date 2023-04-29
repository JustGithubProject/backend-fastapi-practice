from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.database import get_db
from .. import schemas
from .. import models
from ..password_settings import verify_password
from ..token import ACCESS_TOKEN_EXPIRE_MINUTES
from ..token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}