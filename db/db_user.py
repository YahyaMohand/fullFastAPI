from db.hash_pass import Hash
from sqlalchemy.orm.session import Session
from exception import StoryException
from shemas import UserBase
from db.models import User
from typing import Optional
from fastapi import HTTPException, status


def create_user(db: Session, request: UserBase):
    if request.email.startswith(request.email.capitalize()):
        raise StoryException('please dont use first letter capital')
    new_user = User(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_user(db : Session):
    return db.query(User).all()

def get_user(db: Session, id : int ):
    user = db.query(User).filter(User.id == id).first()
    if not user :
        raise StoryException(f"the id {id} not found")
    return user

def get_user_name(db: Session, username : str ):
    user = db.query(User).filter(User.username == username).first()
    if not user :
        raise StoryException(f"the username {username} not found")
    return user

def updates_user(db: Session, id : int, request : UserBase):
    user = db.query(User).filter(User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f"User {id} is not Found")
    user.update({
        User.username : request.username,
        User.email : request.email,
        User.password : Hash.bcrypt(request.password)
    })
    db.commit()
    return "Update done ok!!"

def delete_user(db: Session, id: int):
    user =  db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail= f"User {id} is not Found"
        )
    db.delete(user)
    db.commit()
    return "deleted"