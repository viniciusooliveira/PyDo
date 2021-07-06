from typing import Optional, Iterable
from fastapi import Depends
from app.domain.models import Todo
from app.infra.db.repositories.list_repository import ListRepository, get_instance as repo_instance


class ListBusiness:

    _repo = None

    def __init__(self, repo: ListRepository):
        self._repo = repo

    async def exists_by_id(self, id_: int) -> bool:
        return await self._repo.exists_by_id(id_)

    async def get(self, id_: int) -> Optional[Todo]:
        return await self._repo.get(id_)

    async def get_all(self) -> Iterable[Todo]:
        return await self._repo.get_all()

    async def save(self, model: Todo) -> Todo:
        return await self._repo.save(model)

    async def delete(self, id_: int) -> bool:
        return await self._repo.delete(id_)


def get_instance(repo: ListRepository = Depends(repo_instance)):
    return ListBusiness(repo)
