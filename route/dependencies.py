from email import header
from fastapi import FastAPI, APIRouter,Request, Depends

router = APIRouter(
    prefix='/dependencies',
    tags=['dependencies']
)


def convert_header(req :  Request, seperator : str = "--"):
    out_header = []
    for key, value in req.headers.items():
        out_header.append(f"{key} {seperator} {header}")
    return out_header

@router.get('/')
def get_items(seperator : str = "--", header = Depends(convert_header)):
    return {
        "header" : header,
        "seperator" : seperator
    }


class Account():
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email



@router.post('/user')
def create_user(name : str, email: str,password: str, account: Account = Depends()):
    return {
        account
    }