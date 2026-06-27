from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


# temporary database, which will be replaced with database like SQLite
temp_db = [

{
  "id": 1,
  "title": "t1",
  "description": "t1di",
  "done": True
},
{
  "id": 2,
  "title": "t1",
  "description": "t1di",
  "done": True
},
{
  "id": 3,
  "title": "t1",
  "description": "t1di",
  "done": True
}
]


# CreateTask class for the structure of the task's data

class CreateTask(BaseModel):
    title:str
    description:str
    done:bool = False


# UpdateTask class for the structure of the tasks to be updated

class UpdateTask(BaseModel):
    title:str
    description:str
    done:bool



# Create Task

@app.post("/task")
async def add_task(task:CreateTask):
    mytask = {"id":len(temp_db)+1,"title":task.title,"description":task.description,"done":task.done}
    temp_db.append(mytask)
    return mytask    

# Read Task

@app.get("/")
async def get_all_tasks():
    return temp_db



# Update Task

@app.put("/task/{id}")
async def update_task(id:int,valueUpdate:UpdateTask):
    for index,task in enumerate(temp_db):
        if task["id"] == id:
            temp_db[index] = {"id":id,"title": valueUpdate.title,"description":valueUpdate.description,"done":valueUpdate.done}
            return{"message":"Task updated"}
    return{"message":"Task not found"}

# Delete task

@app.delete("/delete/{id}")
async def delete_task(id:int):
    for index,task in enumerate(temp_db):
        if task["id"] == id:
            temp_db.pop(index)
            return {"message":"Task Deleted"}
    return {"message":"Task not found"}
