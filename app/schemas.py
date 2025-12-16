from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum


# #---------------User Schemas---------------#
# class UserCreate(BaseModel):
#     username: str
#     email: str
#     password: str

# class UserRead(BaseModel):
#     id: int
#     username: str
#     email: str
#     is_active: int

#     class Config:
#         orm_mode = True

# #--------------Task Schemas---------------#
# #str is used here to ensure compatibility with JSON serialization and
# #Enum is used to define a set of named values.
# class TaskStatus(str, Enum):
#     TODO = "TODO"
#     IN_PROGRESS = "IN_PROGRESS"
#     COMPLETED = "COMPLETED"

# class TaskCreate(BaseModel):
#     title: str
#     description: Optional[str] = None
#     status: Optional[TaskStatus] = TaskStatus.TODO

# class TaskUpdate(BaseModel):
#     title: Optional[str] = None
#     description: Optional[str] = None
#     status: Optional[TaskStatus] = TaskStatus.TODO

# class TaskRead(BaseModel):
#     id: int
#     title: str
#     description: Optional[str] = None
#     status: TaskStatus
#     owner_id: int
#     created_at: datetime

#     class Config:
#         orm_mode = True

'''In schemas.py, create request/response models:
UserCreate, UserRead
TaskCreate, TaskUpdate, TaskRead
These ensure clean validation and serialization.'''

#---------------User Schemas---------------#
class UserCreate(BaseModel):
    username: str
    hashed_password: str
    created_at: datetime

class UserRead(BaseModel):
    id: int
    username: str
    created_at: datetime

    class Config:
        orm_mode = True
    
#--------------Task Schemas---------------#
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
        orm_mode = True