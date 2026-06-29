from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from database import Base, get_db, engine
from sqlalchemy.orm import Session
from models import Task


Base.metadata.create_all(bind = engine)

app = FastAPI()

# pydantic models

class TaskCreate(BaseModel):
    title:str
    description:str
    done:bool = False

class TaskUpdate(BaseModel):
    title:str
    description:str
    done:bool

class TaskResponse(BaseModel):
    id:int
    title:str
    description:str
    done:bool


    class config():
        form_attributes = True



