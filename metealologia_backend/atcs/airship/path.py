from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

path_router = APIRouter(prefix="/path")


class Beacon(BaseModel):
    id: str
    longitude: float
    latitude: float


class ManualControl(BaseModel):
    speed: float
    direction: float


@path_router.get("", response_model=list[Beacon])
async def get_airship_path():
    """Get the list of destinations"""
    raise HTTPException(501)


@path_router.put("")
async def set_airship_path(beacons: list[Beacon]):
    """Set the list of destinations"""
    raise HTTPException(501)


@path_router.put("/manual")
async def set_airship_path_manual(manual: ManualControl):
    """Override the autopilot"""
    raise HTTPException(501)


@path_router.patch("/manual")
async def modify_airship_path_manual(manual: ManualControl):
    """Modify manual control parameters"""
    raise HTTPException(501)


@path_router.delete("/manual")
async def cancel_airship_path_manual():
    """Return to autopilot"""
    raise HTTPException(501)