from typing import Sequence

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ...models.dataset_product import DatasetProduct
from ..dependencies import get_db_session
from .generic_routes import create_generic_list_handler
from .query_params import DatasetProductQueryParams

router = APIRouter(prefix="/dataset_products")

# Create the generic handler
_list_handler = create_generic_list_handler(DatasetProduct, "dataset products")


@router.get("")
async def get_dataset_product_list(
    query: DatasetProductQueryParams = Depends(),
    session: AsyncSession = Depends(get_db_session),
) -> Sequence[DatasetProduct]:
    return await _list_handler(session, **query.model_dump(exclude_none=True))
