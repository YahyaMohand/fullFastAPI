from fastapi import FastAPI, APIRouter,status,Response
from enum import Enum
from typing import Optional


router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


@router.get("/items/{item_id}", tags=['blog'])
def read_item(item_id):
    return {"item_id": f"My item_id is {item_id}"}


@router.get("/{id}/comments/{comment_id}", tags=['comments'])
def blog_comment(id : int, comment_id: int, valid: bool, user_name: Optional[str] = None):
    return {
        "message" : f"the id {id} comment_id {comment_id} valid {valid} username {user_name} "
    }

class BlogType(str ,Enum):
    short = "short"
    many = "many"
    how_to = "how_to"

@router.get("/type/{type}")
def type_blog(type : BlogType):
    return {
        "message" : f"the type is {type}"
    }

@router.get("/{id}", status_code = status.HTTP_200_OK)
def blog(id : int, response: Response):
    if id > 5 :
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message" : f"the blog {id} not found "}
    else :
        response.status_code = status.HTTP_200_OK
        return {"message" : f"the id is {id}"}
