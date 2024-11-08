import asyncio
from fastapi import Depends
from typing import Annotated
from sqlmodel import SQLModel
from urllib.parse import urlparse
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from .config import Config

tmpPostgres = urlparse(Config.DATABASE_URL)

async_engine = create_async_engine(
    url=f"postgresql+asyncpg://{tmpPostgres.username}:{tmpPostgres.password}@{tmpPostgres.hostname}{tmpPostgres.path}?ssl=require", echo=True)


async def init_db() -> None:
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session():
    Session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with Session() as session:
        yield session

db_dependency = Annotated[AsyncSession, Depends(get_session)]
