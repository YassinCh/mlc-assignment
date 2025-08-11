from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from ..settings import AppSettings


def init_async_engine(
    settings: AppSettings,
) -> tuple[AsyncEngine, async_sessionmaker[AsyncSession]]:
    async_engine = create_async_engine(
        settings.database_url.unicode_string(), echo=False, future=True
    )
    async_session_factory = async_sessionmaker(
        async_engine,
        autoflush=False,
        expire_on_commit=False,
    )

    return async_engine, async_session_factory
