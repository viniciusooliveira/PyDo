from __future__ import annotations
from typing import Optional, Type, Any
from pydantic import BaseModel, Field


class Todo(BaseModel):
    id: int = Field(42,
                    title="Id",
                    description="Todo Identifier")
    name: str = Field("Buy a PS5",
                      title="Name",
                      description="Todo name, insert something that reminds you of the task to be done")
    done: bool = Field("true",
                       title="Done",
                       description="Tells the task is done or not")
    priority: Optional[int] = Field(1,
                                    title="Priority",
                                    description="Tells the task level of priority", )
    list_id: int = Field(1,
                         title="List ID",
                         description="Tells which list the item belongs to")

    class Config:
        orm_mode = True
