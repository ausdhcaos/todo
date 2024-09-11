from typing import AsyncGenerator
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
import settings as settings


engine = create_engine(f"postgresql://{settings.DATABASE_CONN_STR}")

async_engine = create_async_engine(
    f"postgresql+asyncpg://{settings.DATABASE_CONN_STR}", echo=settings.ENV == "dev"
)

async_session = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session
