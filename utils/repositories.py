from abc import ABC, abstractmethod
from typing import Any

from core.database import Model, async_session

from sqlalchemy import select, insert, update, delete


class AbstractRepository(ABC):
    @abstractmethod
    async def create(self, **data):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, *where):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self, *where):
        raise NotImplementedError

    @abstractmethod
    async def update(self, *where, **data):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, *where):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model: Model | Any = None  # type: ignore

    async def create(self, **data):
        async with async_session() as session:
            try:
                stmt = insert(self.model).values(**data).returning(self.model.id)  # type: ignore
                result = await session.execute(stmt)
                await session.commit()
                return result.scalar_one()
            except Exception as e:
                await session.rollback()
                raise e

    async def find_one(self, *where):
        async with async_session() as session:
            stmt = select(self.model).where(*where)  # type: ignore
            result = await session.execute(stmt)
            return result.scalar_one_or_none()

    async def find_all(self, *where):
        async with async_session() as session:
            stmt = select(self.model).where(*where)  # type: ignore
            result = await session.execute(stmt)
            return result.scalars().all()

    async def update(self, *where, **data):
        async with async_session() as session:
            try:
                stmt = update(self.model).where(*where).values(**data)  # type: ignore
                await session.execute(stmt)
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e

    async def delete(self, *where) -> None:
        async with async_session() as session:
            try:
                stmt = delete(self.model).where(*where)  # type: ignore
                await session.execute(stmt)
                await session.commit()
            except Exception as e:
                await session.rollback()
                raise e
