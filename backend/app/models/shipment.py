from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Shipment(Base):
    __tablename__ = "shipments"

    id = Column(Integer, primary_key=True, index=True)
    pickup_location = Column(String, nullable=False)
    delivery_location = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    status = Column(String, nullable=False)
    driver_id = Column(Integer, nullable=False)
    vehicle_id = Column(Integer, nullable=False)