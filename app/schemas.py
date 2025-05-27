from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    is_done: bool

class Task(TaskBase):
    id: int
    is_done: bool

    class Config:
        orm_mode = True
