from app.domain.models import Todo
from app.infra.db.database import Base
from typing import Union

from sqlalchemy import Column, Integer, VARCHAR, Boolean


class TodoEntity (Base):

    __tablename__ = "todo"

    id: Union[int, Column] = Column(Integer, primary_key=True, autoincrement=True)
    name: Union[str, Column] = Column(VARCHAR(length=255), nullable=False)
    done: Union[bool, Column] = Column(Boolean, nullable=False)

