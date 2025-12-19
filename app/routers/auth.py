from fastapi import APIRouter, Depends, HTTPException, status
from app import schemas, models
from app.database import get_db
from sqlalchemy.orm import Session
from jose import JWTError, jwt


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/users/")
def create_user(user: schemas.UserCreate):
    # TODO: Add DB logic
    return {"message": "User created"}

@router.post("/login/")
def login(user_credentials: schemas.UserLogin):
    # TODO: Add authentication logic
    return {"message": "User logged in"}

