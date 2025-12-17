from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

#To Load Environment Variables
load_dotenv()

#Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL")

#SQLAlchemy Setup
engine = create_engine(DATABASE_URL, echo=False)

#Creating a configured "Session" class for database interactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base class for declarative models what is used to create the database tables
Base = declarative_base()

#Dependency to get DB session this is typically used in web frameworks like 
#FastAPI by calling get_db as a dependency and ensuring proper session management
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
