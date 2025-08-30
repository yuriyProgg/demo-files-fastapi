from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from core.settings import DATABASE_URL


class Model(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
)


async def get_session():
    async with async_session() as session:
        yield session


async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
