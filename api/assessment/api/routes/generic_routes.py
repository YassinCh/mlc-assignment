from typing import Any, Sequence, Type, TypeVar

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel

from ...db.base_service import BaseService

ModelT = TypeVar("ModelT", bound=SQLModel)


def create_generic_list_handler(model_class: Type[ModelT], entity_name: str):
    """
    Creates a reusable list handler function for dataset entities.
    """

    async def list_handler(session: AsyncSession, **filters: Any) -> Sequence[ModelT]:
        active_filters = {k: v for k, v in filters.items() if v is not None}
        items = await BaseService(session, model_class).list(**active_filters)
        if not items:
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"No {entity_name} found")
        return items

    return list_handler
