from typing import Optional, Iterable
from fastapi import Depends
from sqlalchemy.orm import Session, lazyload
from sqlalchemy.orm.exc import NoResultFound
from app.domain.models import List
from app.infra.db.entities import ListEntity
from app.infra.db.database import get_session


class ListRepository:
    _session: Session

    def __init__(self, session: Session):
        self._session = session

    async def exists_by_id(self, id_: int) -> bool:
        return await self._session.query(ListEntity).filter_by(id=id_).exists()

    async def get(self, id_: int) -> Optional[List]:
        try:
            entity = (self._session.query(ListEntity)
                      .options(lazyload("items"))
                      .filter_by(id=id_).one())
        except NoResultFound:
            return None

        return List.from_orm(entity)

    async def get_all(self) -> Iterable[List]:
        results = (self._session.query(ListEntity)
                   .limit(100)
                   .all())
        if len(results) == 0:
            return []

        return [List.from_orm(r) for r in results]

    async def save(self, model: List) -> List:
        entity = None

        if model.id and model.id > 0:
            try:
                entity = self._session.query(ListEntity).filter_by(id=model.id).one()
            except NoResultFound:
                return None

            entity.name = model.name
            entity.done = model.done
        else:
            entity = ListEntity(**model.dict())
            self._session.add(entity)

        self._session.flush()
        self._session.commit()

        return List.from_orm(entity)

    async def delete(self, id_: int) -> bool:
        entity = None
        try:
            entity = self._session.query(ListEntity).filter_by(id=id_).one()
        except NoResultFound:
            return None

        self._session.delete(entity)
        self._session.flush()
        self._session.commit()

        return True


def get_instance(session: Session = Depends(get_session)):
    return ListRepository(session)
