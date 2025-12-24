from fastapi import APIRouter,Depends
from app.database import get_db
from app.routers.auth import get_current_user
from app import schemas,models
from datetime import datetime

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@router.post("/", response_model=schemas.TaskRead)
def create_task(task: schemas.TaskCreate, 
                db=Depends(get_db), 
                current_user: schemas.UserRead = Depends(get_current_user)):
    db_task = models.Task(title=task.title,
                            description=task.description,
                            created_at=str(datetime.now()),
                            updated_at=str(datetime.now()),
                            owner_id=current_user.id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/",response_model=list[schemas.TaskRead])
def read_tasks(db=Depends(get_db),
               current_user: models.User = Depends(get_current_user)):
    tasks = db.query(models.Task).filter(models.Task.owner_id == current_user.id).all()
    return tasks

@router.put("/{task_id}")
def update_task(task_id: int,
                task_update: schemas.TaskUpdate,
                db=Depends(get_db),
                current_user: models.User = Depends(get_current_user)):
    task = db.query(models.Task).filter(models.Task.id == task_id,
                                        models.Task.owner_id == current_user.id).first()
    if not task:
        return {"error": "Task not found or not authorized"}
    if task_update.title is not None:
        task.title = task_update.title
    if task_update.description is not None:
        task.description = task_update.description
    if task_update.status is not None:
        task.status = task_update.status
    task.updated_at = str(datetime.now())
    db.commit()
    db.refresh(task)
    return task