from typing import Optional, List
from fastapi import APIRouter, Response, Header, Form


router = APIRouter(
  prefix='/product',
  tags=['product']
)

products = ['PS5', 'TCL', 'UBS']

@router.get('/all')
def get_all_product():
    data = ' '.join(products)
    return Response(content=data, media_type='text/xml')

@router.get('/withheader')
def get_header(response : Response, custom_header : Optional[List[str]] = Header(None)):
    return products

@router.post('/new')
def get_all(name : str = Form(...)):
    products.append(name)
    return products
