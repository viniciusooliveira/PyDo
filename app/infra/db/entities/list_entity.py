from sqlalchemy.orm import relationship, relation, backref
from app.infra.db.database import Base
from typing import Union
from sqlalchemy import Column, INTEGER, VARCHAR, BOOLEAN
from app.infra.db.entities.todo_entity import TodoEntity


class ListEntity (Base):

    __tablename__ = "list"

    id: Union[int, Column] = Column(INTEGER, primary_key=True, autoincrement=True)
    name: Union[str, Column] = Column(VARCHAR(length=255), nullable=False)
    done: Union[bool, Column] = Column(BOOLEAN, nullable=False)
    items = relation("TodoEntity", back_populates="list", lazy="noload")


