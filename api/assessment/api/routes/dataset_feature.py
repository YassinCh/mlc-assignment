from typing import Sequence

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ...models.dataset_feature import DatasetFeature
from ..dependencies import get_db_session
from .generic_routes import create_generic_list_handler
from .query_params import DatasetFeatureQueryParams

router = APIRouter(prefix="/dataset_features")
_list_handler = create_generic_list_handler(DatasetFeature, "features")


@router.get("")
async def get_dataset_features_list(
    query: DatasetFeatureQueryParams = Depends(),
    session: AsyncSession = Depends(get_db_session),
) -> Sequence[DatasetFeature]:
    """Endpoint to get all dataset features optionally for a specific dataset id"""
    return await _list_handler(session, **query.model_dump(exclude_none=True))
