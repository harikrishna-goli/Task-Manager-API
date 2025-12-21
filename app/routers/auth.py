from fastapi import APIRouter, Depends, HTTPException, status
from app import schemas, models
from app.security import hash_password, create_access_token
from app.database import get_db
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import datetime


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/users/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    userexists = (
        db.query(models.User)
                  .filter(models.User.username == user.username)
                  .first())
    
    if userexists:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Username already registered")
    
    hashed_password = hash_password(user.password)
    db_user = models.User(username=user.username, 
                          hashed_password=hashed_password, 
                          created_at=str(datetime.now()))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login/")
def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    user = (db.query(models.User)
            .filter(models.User.username == user_credentials.username)
            .first())
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid username or password")
    access_token = create_access_token(data=user.username)
    return {"access_token": access_token,
            "token_type": "bearer"}

