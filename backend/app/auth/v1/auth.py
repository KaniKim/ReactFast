from fastapi import APIRouter

from app.auth.v1.request.auth import LoginRequest

router = APIRouter()

@router.post("/login/", status_code=200)
async def login(login_info: LoginRequest):
    pass

@router.post("/login/refresh/", status_code=200)
async def login_refresh(refresh_token, request):
    pass