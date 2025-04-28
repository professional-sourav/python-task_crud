from pydantic import BaseModel
import uuid

tasks = []

class Task(BaseModel):
    id: uuid.UUID = None
    name: str
    description: str = None
    completed: bool = False

def create_new_task(new_task: Task):
    new_task.id = uuid.uuid4()
    tasks.append(new_task)
    return tasks

def get_all_tasks():
    return tasks

def remove_a_task(task_id: str):
    try:
        task_id = uuid.UUID(task_id)
    except ValueError:
        print("Invalid task id!")
        return None

    if tasks.count == 0:
        return None

    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return task

    return None
