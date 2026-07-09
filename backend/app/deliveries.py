from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class DeliveryRequest(BaseModel):
    customer_name: str
    address: str
    status: str

@router.get("/")
def get_deliveries():
    return {"message": "Deliveries Retrieved Successfully"}

@router.post("/")
def create_delivery(delivery: DeliveryRequest):
    return {"message": "Delivery Created Successfully", "data": delivery}

@router.put("/{delivery_id}")
def update_delivery(delivery_id: int, delivery: DeliveryRequest):
    return {"message": f"Delivery {delivery_id} Updated Successfully"}

@router.delete("/{delivery_id}")
def delete_delivery(delivery_id: int):
    return {"message": f"Delivery {delivery_id} Deleted Successfully"}