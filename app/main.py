from typing import Optional


from fastapi import FastAPI, status
from pydantic import BaseModel


class PostIn(BaseModel):
    title: str
    body: str


app = FastAPI()


posts_db: list = list()


@app.get("/posts")
async def posts():
    return posts_db


@app.get("/posts/{post_id}")
async def read_post(post_id: int):
    return posts_db[post_id]


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostIn):
    posts_db.append(post)
    return post
