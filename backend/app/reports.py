from fastapi import APIRouter

router = APIRouter()

@router.get("/daily")
def daily_report():
    return {"message": "Daily Report Generated"}

@router.get("/weekly")
def weekly_report():
    return {"message": "Weekly Report Generated"}

@router.get("/monthly")
def monthly_report():
    return {"message": "Monthly Report Generated"}