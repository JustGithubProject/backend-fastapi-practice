from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import Response
from sqlalchemy.orm import Session

from blog.database.database import get_db
from blog import schemas
from blog.oauth2 import get_current_user
from blog.repository.blog import get_everything
from blog.repository.blog import create
from blog.repository.blog import delete
from blog.repository.blog import update
from blog.repository.blog import show_by_id

router_blog = APIRouter(tags=['Blog'])


@router_blog.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(blog: schemas.Blog, db: Session = Depends(get_db),
                get_current_user_1: schemas.User = Depends(get_current_user)  ):
    return create(blog, db)


@router_blog.delete("/blog/{id_el}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id_el: int, db: Session = Depends(get_db),
                get_current_user_1: schemas.User = Depends(get_current_user)):
    return delete(id_el, db)


@router_blog.put("/blog/{id_}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id_: int, request: schemas.Blog, db: Session = Depends(get_db),
                get_current_user_1: schemas.User = Depends(get_current_user)):
    return update(id_, request, db)


@router_blog.get("/blog")
def get_all(get_current_user_1: schemas.User = Depends(get_current_user), db: Session = Depends(get_db)):
    return get_everything(db)


@router_blog.get("/blog/{id_el}", status_code=200, response_model=schemas.ShowBlog)
def show(id_el: int, response: Response, db: Session = Depends(get_db),
         get_current_user_1: schemas.User = Depends(get_current_user)):
    return show_by_id(id_el, response, db)
