from fastapi import FastAPI

from blog.database.database import engine
from blog.database.database import Base
from blog.routers import blog
from blog.routers import user
from blog.routers import authentication

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(blog.router_blog)
app.include_router(user.router_user)
app.include_router(authentication.router)
