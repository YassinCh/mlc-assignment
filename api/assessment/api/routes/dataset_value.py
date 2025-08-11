from typing import Sequence

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ...models.dataset_value import DatasetValue
from ..dependencies import get_db_session
from .generic_routes import create_generic_list_handler
from .query_params import DatasetValueQueryParams

router = APIRouter(prefix="/dataset_values")

# Create the generic handler
_list_handler = create_generic_list_handler(DatasetValue, "values")


@router.get("")
async def get_dataset_values(
    query: DatasetValueQueryParams = Depends(),
    session: AsyncSession = Depends(get_db_session),
) -> Sequence[DatasetValue]:
    return await _list_handler(session, **query.model_dump(exclude_none=True))
