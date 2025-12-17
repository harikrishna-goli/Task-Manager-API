from fastapi import FastAPI
from app import models, schemas, database

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Task Manager API is running"}

@app.post("/users/")
def create_user(User: schemas.UserCreate):
    
    return {"message": "User created"}

@app.post("/tasks/")
def create_task():
    return {"message": "Task created"}

@app.get("/tasks/")
def read_tasks():
    return {"message": "List of tasks"}

@app.put("/tasks/{task_id}")
def update_task(task_id: int):
    return {"message": f"Task {task_id} updated"}

