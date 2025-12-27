from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class TaskModel(BaseModel):
    name: str
    description: str
    done: bool = False

tasks = []

app = FastAPI()

@app.get("/")
def index():
    return {"message": "To Do API!"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def post_tasks(task: TaskModel):
    tasks.append(task)
    return {"message": f"задача создана под номером {len(tasks)-1}"}

@app.delete("/tasks/{task_id}")
def delete_tasks(task_id: int):
    if task_id < 0 or task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Задача не найдена")
    deleted_task = tasks.pop(task_id)
    return {"message": f"задача '{deleted_task.name}' с id {task_id} удалена"}