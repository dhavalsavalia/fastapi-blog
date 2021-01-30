from sqlalchemy.orm import Session


from . import models, schemas


def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def get_posts(db: Session, skip: int = 0):
    return db.query(models.Post).offset(skip).all()


def create_post(db: Session, post: schemas.PostCreate):
    db_item = models.Post(**post.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
