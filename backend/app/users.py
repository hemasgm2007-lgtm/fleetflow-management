from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter()

class UserRequest(BaseModel):
    name: str
    email: EmailStr
    phone: str

@router.get("/")
def get_users():
    return {"message": "Users Retrieved Successfully"}

@router.post("/")
def create_user(user: UserRequest):
    return {"message": "User Created Successfully", "data": user}

@router.put("/{user_id}")
def update_user(user_id: int, user: UserRequest):
    return {"message": f"User {user_id} Updated Successfully"}

@router.delete("/{user_id}")
def delete_user(user_id: int):
    return {"message": f"User {user_id} Deleted Successfully"}