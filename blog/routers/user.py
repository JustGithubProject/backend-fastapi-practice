from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from blog.database.database import get_db
from blog import schemas
from blog import models
from blog.repository.user import create
from blog.repository.user import get_all, get_by_id

router_user = APIRouter(tags=["User"])


@router_user.post("/user")
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return create(request, db)


@router_user.get("/user", response_model=List[schemas.ShowUser])
def get_all_users(db: Session = Depends(get_db)):
    return get_all(db)


@router_user.get("/user/{id_}", response_model=schemas.ShowUser)
def get_user_by_id(id_: int, db: Session = Depends(get_db)):
    return get_by_id(id_, db)
