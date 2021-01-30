from typing import List


from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session


from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/posts", response_model=List[schemas.Post])
async def read_posts(skip: int = 0, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip)
    return posts


@app.get("/posts/{post_id}", response_model=schemas.Post)
async def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db=db, post_id=post_id)
    if db_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return db_post


@app.post("/posts", response_model=schemas.Post, status_code=status.HTTP_201_CREATED)
async def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)
