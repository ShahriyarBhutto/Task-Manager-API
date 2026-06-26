from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


temp_db = []
task_id = len(temp_db)

class Task(BaseModel):
    id:int = task_id + 1
    title:str
    description: str
    done:bool = False

class TaskModel(BaseModel):
    title:str
    description:str
    done:bool = False



@app.get("/")
async def get_all_tasks():
    return temp_db


@app.post("/task")
async def add_task(task:TaskModel):
    task = {"title":task.title,"description":task.description,"done":task.done}
    temp_db.append(task)
    return task

@app.put("/task/{id}")
async def update_task(task:Task):
    temp_task = {}
    for task in temp_db:
        if task.id == id:
            pass
    


@app.delete("/delete/{id}")
async def delete_task():
    pass
