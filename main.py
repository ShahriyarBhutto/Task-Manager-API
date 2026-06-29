from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import engine, get_db, Base
from models import Task

# Tables create karo
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Pydantic models
class TaskCreate(BaseModel):
    title: str
    description: str
    done: bool = False

class TaskUpdate(BaseModel):
    title: str
    description: str
    done: bool

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    done: bool

    class Config:
        from_attributes = True


# Routes
@app.get("/")
def get_all_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()


@app.post("/task", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(title=task.title, description=task.description, done=task.done)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@app.put("/task/{id}", response_model=TaskResponse)
def update_task(id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    existing = db.query(Task).filter(Task.id == id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Task not found")
    existing.title = task.title
    existing.description = task.description
    existing.done = task.done
    db.commit()
    db.refresh(existing)
    return existing


@app.delete("/task/{id}")
def delete_task(id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}