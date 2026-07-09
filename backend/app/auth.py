from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter()

class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/register")
def register(user: RegisterRequest):
    return {"message": "User Registered", "data": user}

@router.post("/login")
def login(user: LoginRequest):
    return {"message": "Login Successful"}

@router.get("/profile")
def profile():
    return {"username": "John", "email": "john@example.com"}

@router.post("/logout")
def logout():
    return {"message": "Logged Out"}