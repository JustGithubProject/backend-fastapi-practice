from fastapi import Depends, status, Response
from fastapi import HTTPException
from sqlalchemy.orm import Session
from blog.database.database import get_db
from .. import models
from .. import schemas


def get_everything(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


def create(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def delete(id_el: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id_el)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id - {id_el} is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return "done"


def update(id_: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id_).first()
    if blog:
        blog.title = request.title
        blog.body = request.body
        db.commit()
        return "The model has updated successfully"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id - {id_} is not found")


def show_by_id(id_el: int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id_el).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id_el} isn't available")
    return blog