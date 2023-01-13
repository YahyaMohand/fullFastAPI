from fastapi import HTTPException,status
from sqlalchemy.orm.session import Session
from db.models import Article
from exception import StoryException
from shemas import ArticleBase, ArticleUpdate

def create_article(db: Session, request: ArticleBase):
    if request.content.startswith('yahya'):
        raise StoryException(' no names please')
    new_article = Article(
        title = request.title,
        content = request.content,
        published = request.published,
        user_id = request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_article(db: Session, id: int):
    article = db.query(Article).filter(Article.id == id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f"Article {id} is not Found"
        )
    return article


def update_article(db: Session, id: int,request: ArticleUpdate):
    article = db.query(Article).filter(Article.id == id)
    if not article.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f"Article {id} is not Found"
        )
    article.update({
        Article.title : request.title,
        Article.content : request.content,
        Article.published : request.published,
    })
    db.commit()
    return "update compelete !!!"
