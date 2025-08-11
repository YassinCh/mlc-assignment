from typing import Any, Generic, Sequence, Type, TypeVar
from uuid import UUID

from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel, select

ModelT = TypeVar("ModelT", bound=SQLModel)


class BaseService(Generic[ModelT]):
    def __init__(self, session: AsyncSession, model_class: Type[ModelT]):
        self.session = session
        self.model_class = model_class

    async def _query(self, **filters: Any) -> Result[tuple[ModelT]]:
        """Build and execute a SELECT query with filters."""
        stmt = select(self.model_class)
        for field, value in filters.items():
            if value is not None and hasattr(self.model_class, field):
                stmt = stmt.where(getattr(self.model_class, field) == value)
        return await self.session.execute(stmt)

    async def one_or_none(self, **filters: Any) -> ModelT | None:
        """Get a single instance matching the filters, or None."""
        result = await self._query(**filters)
        return result.scalar_one_or_none()

    async def list(self, **filters: Any) -> Sequence[ModelT]:
        """Get all instances matching the filters."""
        result = await self._query(**filters)
        return result.scalars().all()

    async def create(self, **kwargs: Any) -> ModelT:
        instance = self.model_class(**kwargs)
        self.session.add(instance)
        await self.session.flush()
        await self.session.refresh(instance)
        return instance

    async def get(self, id: UUID) -> ModelT | None:
        """Get a single instance by ID."""
        return await self.one_or_none(id=id)

    async def update(self, id: UUID, **kwargs: Any) -> ModelT | None:
        """Update an instance by ID."""
        instance = await self.get(id)
        if not instance:
            return None
        for key, value in kwargs.items():
            if hasattr(instance, key):
                setattr(instance, key, value)
        self.session.add(instance)
        await self.session.flush()
        await self.session.refresh(instance)
        return instance

    async def delete(self, id: UUID) -> bool:
        """Delete an instance by ID."""
        instance = await self.get(id)
        if not instance:
            return False
        await self.session.delete(instance)
        await self.session.flush()
        return True
