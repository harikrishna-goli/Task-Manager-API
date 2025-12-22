from fastapi import APIRouter, Depends, HTTPException, status
from app import schemas, models
from app.security import hash_password, create_access_token, verify_password, decode_access_token
from app.database import get_db
from sqlalchemy.orm import Session
from datetime import datetime
from jose import JWTError, jwt
from fastapi.security import OAuth2
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

class OAuth2PasswordBearerWithCookie(OAuth2):
    def __init__(self, tokenUrl: str): 
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl})
        super().__init__(flows=flows) 


oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/auth/login")
@router.get("/me/", response_model=schemas.UserRead)
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    username = decode_access_token(token)
    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
            )

    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="User not found")
    return user

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
    if not user or not verify_password(plain_password=user_credentials.password,
                                       hashed_password=user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Invalid username or password")
    access_token = create_access_token(data=user.username)
    return {"access_token": access_token, 
            "token_type": "bearer"}

