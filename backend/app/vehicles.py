from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class VehicleRequest(BaseModel):
    vehicle_number: str
    vehicle_type: str
    capacity: int
    status: str

@router.get("/")
def get_vehicles():
    return {"message": "Vehicles Retrieved Successfully"}

@router.post("/")
def create_vehicle(vehicle: VehicleRequest):
    return {"message": "Vehicle Added Successfully", "data": vehicle}

@router.put("/{vehicle_id}")
def update_vehicle(vehicle_id: int, vehicle: VehicleRequest):
    return {"message": f"Vehicle {vehicle_id} Updated Successfully"}

@router.delete("/{vehicle_id}")
def delete_vehicle(vehicle_id: int):
    return {"message": f"Vehicle {vehicle_id} Deleted Successfully"}