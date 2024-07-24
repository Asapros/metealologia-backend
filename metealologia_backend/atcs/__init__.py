from fastapi import APIRouter, HTTPException

from .airship import airship_router

atcs_router = APIRouter(prefix="/atcs", tags=["ATCS"])
atcs_router.include_router(airship_router)


@atcs_router.get("", response_model=list)
async def get_all_airships():
    """Returns a list of connected airships"""
    raise HTTPException(501)
