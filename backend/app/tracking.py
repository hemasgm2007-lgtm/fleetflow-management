from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TrackingRequest(BaseModel):
    vehicle_id: int
    latitude: float
    longitude: float
    speed: float

@router.get("/")
def get_tracking():
    return {"message": "Tracking Details Retrieved Successfully"}

@router.post("/")
def update_tracking(track: TrackingRequest):
    return {"message": "Tracking Updated Successfully", "data": track}