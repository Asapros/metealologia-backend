from fastapi import APIRouter, HTTPException

from .path import path_router

airship_router = APIRouter(prefix="/{airship_id}")
airship_router.include_router(path_router)


@airship_router.get("")
async def get_airship_data():
    raise HTTPException(501)

