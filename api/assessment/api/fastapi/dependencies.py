from collections.abc import AsyncGenerator

from fastapi import Depends
from starlette.requests import Request
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncConnection, AsyncSession, async_sessionmaker


def _get_db_connection(request: Request) -> AsyncEngine:
    return request.app.state.async_engine


def _get_db_session(request: Request) -> async_sessionmaker[AsyncSession]:
    return request.app.state.async_session_factory


async def get_db_connection(
    engine: AsyncEngine = Depends(_get_db_connection),
) -> AsyncGenerator[AsyncConnection, None]:
    async with engine.connect() as conn:
        yield conn
    

async def get_db_session(
    session_factory: async_sessionmaker[AsyncSession] = Depends(_get_db_session),
) -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session
