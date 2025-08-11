from typing import Tuple

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from assessment.settings import AppSettings


class Base(DeclarativeBase):
    pass


def init_async_engine(
    settings: AppSettings
) -> Tuple[AsyncEngine, async_sessionmaker[AsyncSession]]:
    async_engine = create_async_engine(
        settings.database_url.unicode_string(),
        echo=False,
        future=True
    )
    async_session_factory = async_sessionmaker(
        async_engine,
        autoflush=False,
        expire_on_commit=False,
    )

    return async_engine, async_session_factory