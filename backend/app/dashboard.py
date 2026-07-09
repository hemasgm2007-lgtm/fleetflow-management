from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def dashboard():
    return {
        "total_vehicles": 50,
        "total_drivers": 20,
        "active_trips": 15,
        "completed_deliveries": 120
    }