from fastapi import FastAPI
from app.database import engine, Base
from app.routers.auth import router as auth_router

# Import new routers
from app.routers.users import router as users_router
from app.routers.vehicles import router as vehicles_router
from app.routers.drivers import router as drivers_router
from app.routers.shipments import router as shipments_router
from app.routers.tracking import router as tracking_router

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Existing Authentication router
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])

# New routers
app.include_router(users_router)
app.include_router(vehicles_router)
app.include_router(drivers_router)
app.include_router(shipments_router)
app.include_router(tracking_router)

@app.get("/")
def home():
    return {"message": "FleetFlow Backend Connected Successfully"}