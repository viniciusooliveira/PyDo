from sqlalchemy.orm import relationship
from app.infra.db.database import Base
from typing import Union
from sqlalchemy import Column, Integer, VARCHAR, Boolean, ForeignKey


class TodoEntity (Base):

    __tablename__ = "todo"

    id: Union[int, Column] = Column(Integer, primary_key=True, autoincrement=True)
    name: Union[str, Column] = Column(VARCHAR(length=255), nullable=False)
    done: Union[bool, Column] = Column(Boolean, nullable=False)
    priority: Union[int, Column] = Column(Integer, nullable=True, index=True)
    list_id: Union[int, Column] = Column(Integer, ForeignKey('list.id', ondelete="CASCADE"), nullable=False)
    list = relationship("ListEntity", back_populates="items", lazy="noload")


