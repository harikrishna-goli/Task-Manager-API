from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


'''
Set up database models
Create a models.py file with SQLAlchemy models for your core entities:
User (id, username, hashed_password, created_at)
Task (id, title, description, status, owner_id, created_at, updated_at)
Link Task.owner_id to User.id with a foreign key.
'''


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="owner")

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, default="TODO", nullable=False)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(String, nullable=False)
    updated_at = Column(String, nullable=True)

    owner = relationship("User", back_populates="tasks")
