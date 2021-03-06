from typing import Optional, Iterable
from fastapi import Depends
from sqlalchemy.orm import Session, lazyload
from sqlalchemy.orm.exc import NoResultFound
from app.domain.models import Todo
from app.infra.db.entities import TodoEntity, ListEntity
from app.infra.db.database import get_session


class TodoRepository:
    _session: Session

    def __init__(self, session: Session):
        self._session = session

    async def exists_by_id(self, id_: int) -> bool:
        return await self._session.query(TodoEntity).filter_by(id=id_).exists()

    async def get(self, id_: int) -> Optional[Todo]:
        try:
            entity = (self._session.query(TodoEntity)
                      .options(lazyload("list"))
                      .filter_by(id=id_).one())
        except NoResultFound:
            return None

        return Todo.from_orm(entity)

    async def get_all(self) -> Iterable[Todo]:
        results = (
            self._session.query(TodoEntity)
            .limit(100)
            .all()
        )
        if len(results) == 0:
            return []

        return [Todo.from_orm(r) for r in results]

    async def save(self, model: Todo) -> Todo:
        entity = None

        if model.id and model.id > 0:
            try:
                entity = self._session.query(TodoEntity).filter_by(id=model.id).one()
            except NoResultFound:
                return None

            entity.name = model.name
            entity.done = model.done
            entity.priority = model.priority
        else:
            try:
                entity = TodoEntity(**model.dict())
                entity.list = self._session.query(ListEntity).filter_by(id=entity.list_id).one()
                self._session.add(entity)
            except NoResultFound:
                return None

        self._session.flush()
        self._session.commit()

        return Todo.from_orm(entity)

    async def delete(self, id_: int) -> bool:
        entity = None
        try:
            entity = self._session.query(TodoEntity).filter_by(id=id_).one()
        except NoResultFound:
            return None

        self._session.delete(entity)
        self._session.flush()
        self._session.commit()

        return True


def get_instance(session: Session = Depends(get_session)):
    return TodoRepository(session)
