# app/main.py
from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from . import models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency: DBセッションの取得とクローズ
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/v1/tasks", response_model=List[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    """Get all tasks"""
     # query関数でmodels.pyで定義したモデルを指定し、.all()関数ですべてのレコードを取得
    tasks = db.query(models.Task).all()
    return tasks

@app.post("/api/v1/tasks", response_model=schemas.TaskResponse, status_code=201)
def create_task(
    task: schemas.TaskCreate, 
    db: Session = Depends(get_db)
):
    """Create a new task"""
    db_task = models.Task(
        title=task.title,
        description=task.description,
        isDone=False
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/api/v1/tasks/{task_id}", response_model=schemas.TaskResponse)
def get_task(
    task_id: int, 
    db: Session = Depends(get_db)
):
    """Get a task by ID"""
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@app.put("/api/v1/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int, 
    task_update: schemas.TaskUpdate, 
    db: Session = Depends(get_db)
):
    """Update a task by ID"""
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db_task.title = task_update.title
    db_task.description = task_update.description
    db_task.isDone = task_update.isDone
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/api/v1/tasks/{task_id}", status_code=204)
def delete_task(
    task_id: int, 
    db: Session = Depends(get_db)
):
    """Delete a task by ID"""
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_task)
    db.commit()
    return
