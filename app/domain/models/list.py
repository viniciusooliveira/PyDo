import typing
from pydantic import BaseModel, Field

from app.domain.models.todo import Todo


class List(BaseModel):
    id: int = Field(42,
                    title="Id",
                    description="Todo Identifier")
    name: str = Field("Buy a PS5",
                      title="Name",
                      description="Todo name, insert something that reminds you of the task to be done")
    done: bool = Field("true",
                       title="Done",
                       description="Tells the task is done or not")

    items: typing.Optional[typing.List[Todo]] = Field(None,
                                                     title="Items",
                                                     description="Items")

    class Config:
        orm_mode = True
