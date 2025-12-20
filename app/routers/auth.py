from fastapi import APIRouter, Depends, HTTPException, status
from app import schemas, models
from app.security import hash_password
from app.database import get_db
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import datetime


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hash_password = hash_password(user.password)
    db_user = models.User(username=user.username, 
                          hashed_password=hash_password, 
                          created_at=str(datetime.now()))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login/")
def login(user_credentials: schemas.UserLogin):
    # TODO: Add authentication logic
    return {"message": "User logged in"}

