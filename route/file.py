from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
import shutil


router = APIRouter(
    prefix='/file',
    tags=['file']
)


@router.post('/')
def post_file(file: bytes = File(...)):
    content = file.decode('utf-8')
    lines = content.split('\n')
    return lines


@router.post('/uploadfile')
def upload(upload_file : UploadFile = File(...)):
    path = f"files/{upload_file.filename}"
    with open(path, 'w+b') as buffer :
        shutil.copyfileobj(upload_file.file, buffer)

    return {
        'filename' : path,
        'type' : upload_file.content_type,
        'data' : upload_file.headers
    }

@router.get('/download/{name}', response_class=FileResponse)
def get_file(name : str):
    path = f'files/{name}'
    return path