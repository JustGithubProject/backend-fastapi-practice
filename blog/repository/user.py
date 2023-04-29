from fastapi import Depends
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from blog import models
from blog import schemas
from blog.database.database import get_db
from blog.password_settings import pwd_context


def create(request: schemas.User, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


def get_by_id(id_: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id_).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the id {id_} isn't available")
    return user