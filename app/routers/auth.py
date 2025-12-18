from fastapi import APIRouter, Depends
from app import schemas
from app.database import get_db

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

