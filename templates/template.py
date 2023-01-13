from fastapi import FastAPI,APIRouter,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix='/template', tags=['template'])

template = Jinja2Templates(directory="templates")

@router.post('/products/{id}', response_class=HTMLResponse)
def get_product(id : str, request: Request):
    return template.TemplateResponse(
        "products.html",
        {
            'request' : request,
            'id' : id
        }
    )
