from fastapi import FastAPI
from app.database import engine, Base

from app.auth import router as auth_router
from app.users import router as users_router
from app.vehicles import router as vehicles_router
from app.drivers import router as drivers_router
from app.trips import router as trips_router
from app.deliveries import router as deliveries_router
from app.tracking import router as tracking_router
from app.reports import router as reports_router
from app.dashboard import router as dashboard_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FleetFlow Backend")

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(vehicles_router, prefix="/vehicles", tags=["Vehicles"])
app.include_router(drivers_router, prefix="/drivers", tags=["Drivers"])
app.include_router(trips_router, prefix="/trips", tags=["Trips"])
app.include_router(deliveries_router, prefix="/deliveries", tags=["Deliveries"])
app.include_router(tracking_router, prefix="/tracking", tags=["Tracking"])
app.include_router(reports_router, prefix="/reports", tags=["Reports"])
app.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])

@app.get("/")
def home():
    return {"message": "FleetFlow Backend Connected Successfully"}