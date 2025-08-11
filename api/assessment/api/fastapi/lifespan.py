from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from assessment.db.sqlalchemy import init_async_engine
from assessment.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    async_engine, async_session_factory = init_async_engine(settings)
    app.state.async_engine = async_engine
    app.state.async_session_factory = async_session_factory
    yield
    await app.state.async_engine.dispose()