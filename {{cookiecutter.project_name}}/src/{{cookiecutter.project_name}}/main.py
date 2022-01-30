from typing import List

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseSettings
from sqlalchemy.orm import Session

from {{cookiecutter.package_name}} import schemas, crud
from {{cookiecutter.package_name}}.database import SessionLocal

app = FastAPI()


class Settings(BaseSettings):
    app_name: str = "{{cookiecutter.package_name}}"


settings = Settings()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/micro_blog_posts/", response_model=schemas.MicroBlogPost)
def create_repo_for_user(
    user_id: int, micro_blog_post: schemas.MicroBlogPostCreate, db: Session = Depends(get_db)
):
    post = crud.create_user_micro_blog_post(db, micro_blog_post, user_id)
    return post


@app.get("/micro_blog_posts/", response_model=List[schemas.MicroBlogPost])
def read_repos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    repos = crud.get_micro_blog_posts(db, skip=skip, limit=limit)
    return repos
