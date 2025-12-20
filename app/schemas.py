from pydantic import BaseModel, constr
from typing import List, Optional, Annotated
from datetime import datetime
from enum import Enum

'''In schemas.py, create request/response models:
UserCreate, UserRead
TaskCreate, TaskUpdate, TaskRead
These ensure clean validation and serialization.'''

#---------------User Schemas---------------#

#To Create a new user input schema
class UserCreate(BaseModel):
    username: str
    password: Annotated[str, constr(min_length=8, max_length=72)]  

#Create a user output schema for reading user data after creation
class UserRead(BaseModel):
    id: int
    username: str
    created_at: datetime

    class Config:
        from_attributes = True

#Schema for user login
class UserLogin(BaseModel):
    username: str
    password: str

    
#--------------Task Schemas---------------#
#Enum for task status
class TaskStatus(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[TaskStatus] = TaskStatus.TODO
    created_at: datetime

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    updated_at: Optional[datetime] = None

class TaskRead(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: TaskStatus
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True