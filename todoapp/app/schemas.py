from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: str
    description: str | None = None
    isDone: bool

class TaskResponse(TaskBase):
    id: int
    isDone: bool

    class Config:
        orm_mode = True
