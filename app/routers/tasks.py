from fastapi import APIRouter

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@router.post("/")
def create_task():
    return {"message": "Task created"}

@router.get("/")
def read_tasks():
    return {"message": "List of tasks"}

@router.put("/{task_id}")
def update_task(task_id: int):
    return {"message": f"Task {task_id} updated"}
