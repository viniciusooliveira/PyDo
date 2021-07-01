from pydantic import BaseModel, Field


class Todo (BaseModel):

    id: int = Field(42,
                    title="Id",
                    description="Todo Identifier")
    name: str = Field("Buy a PS5",
                      title="Name",
                      description="Todo name, insert something that reminds you of the task to be done")
    done: bool = Field("true",
                       title="Done",
                       description="Tells the task is done or not")

    class Config:
        orm_mode = True
