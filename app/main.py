from fastapi import FastAPI
from app.routers import auth, tasks

app = FastAPI()

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Task Manager API is running"}