from fastapi import APIRouter, Depends
from .dependencies import CurrUserBearer

auth_router = APIRouter()


@auth_router.get("")
async def profile_me(user_details: dict = Depends(CurrUserBearer())):
    return user_details
