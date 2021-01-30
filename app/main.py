from fastapi import FastAPI, status
from pydantic import BaseModel


class Post(BaseModel):
    title: str
    body: str


app = FastAPI()


@app.get("/posts")
async def posts():
    return {"posts": ["First Post"]}


@app.get("/posts/{post_id}")
async def read_post(post_id: int):
    return {"post_id": post_id}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    return post


