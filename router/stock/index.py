from fastapi import APIRouter

router = APIRouter()

@router.get('/')
def api():
    return {'msg':"stock Connect OK"}

@router.get('/investor/{type}')
def api1(type):
    return {'name':type}