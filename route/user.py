from typing import List,Optional
from shemas import UserBase, UserDisplay
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from db.database import get_db
from sqlalchemy.orm import Session
from db import db_user
from auth.oauth2 import get_current_user

router = APIRouter(prefix='/user', tags=['user'])

@router.post('/', response_model = UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

@router.get('/' , response_model=List[UserDisplay])
def read_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_user(db)

@router.get('/{id}', response_model=UserDisplay)
def read_user(id : int,  db: Session = Depends(get_db), current_user : UserBase = Depends(get_current_user)):
    return db_user.get_user(db, id)

@router.put('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.updates_user(db, id, request)

@router.delete('/delete/{id}')
def delete_user(id : int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, id)
    