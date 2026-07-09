from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TripRequest(BaseModel):
    source: str
    destination: str
    vehicle_id: int
    driver_id: int

@router.get("/")
def get_trips():
    return {"message": "Trips Retrieved Successfully"}

@router.post("/")
def create_trip(trip: TripRequest):
    return {"message": "Trip Created Successfully", "data": trip}

@router.put("/{trip_id}")
def update_trip(trip_id: int, trip: TripRequest):
    return {"message": f"Trip {trip_id} Updated Successfully"}

@router.delete("/{trip_id}")
def delete_trip(trip_id: int):
    return {"message": f"Trip {trip_id} Deleted Successfully"}