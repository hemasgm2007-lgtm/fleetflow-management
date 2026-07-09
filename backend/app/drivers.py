from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class DriverRequest(BaseModel):
    name: str
    license_number: str
    phone: str
    experience: int

@router.get("/")
def get_drivers():
    return {"message": "Drivers Retrieved Successfully"}

@router.post("/")
def create_driver(driver: DriverRequest):
    return {"message": "Driver Added Successfully", "data": driver}

@router.put("/{driver_id}")
def update_driver(driver_id: int, driver: DriverRequest):
    return {"message": f"Driver {driver_id} Updated Successfully"}

@router.delete("/{driver_id}")
def delete_driver(driver_id: int):
    return {"message": f"Driver {driver_id} Deleted Successfully"}