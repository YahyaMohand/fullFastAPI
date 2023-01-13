from typing import Optional,List, Dict
from fastapi import APIRouter,Query, Body, Path
from pydantic import BaseModel

router = APIRouter(prefix='/blog', tags=['post'])


class BlogModel(BaseModel):
    username : str
    password : str
    email_verifiy : Optional[bool]
    tags : List[str] = []
    metadata : Dict[str,str] = {'key' : 'value'}


@router.post('/post/{id}')
def post_id(blog : BlogModel, id : int, version : int = 1):
    return {
        'id' : id,
        'data' : blog,
        'version' : version
        }

@router.post('/post/{id}/comment')
def create_comment(blog : BlogModel, id : int, 
                        comment_id : int = Query(None, 
                        title= "this is comment_id",alias= "commentID" ),
                        content : str = Body(..., 
                                max_length=10,
                                regex="^[a-z\s]*$"),
                        v : Optional[List[str]] = Query(None)
                        ):
    return {
        "id" : id,
        "blog" : blog,
        "comment_id" : comment_id,
        "content" : content
    }
