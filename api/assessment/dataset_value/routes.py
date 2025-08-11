from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from assessment.dataset_value.service import DatasetValueService
from assessment.api.fastapi.dependencies import get_db_session
from assessment.dataset_value.schemas import GetDatasetValueList

router = APIRouter(prefix="/dataset_values")


@router.get("")
async def get_dataset_values(
    product_id: Optional[int] = None,
    feature_id: Optional[int] = None,
    session: AsyncSession = Depends(get_db_session),
):
    service = DatasetValueService(session)
    value_models = await service.list(product_id=product_id, feature_id=feature_id)
    if not value_models:
        raise HTTPException(status_code=404, detail="No values found")
    schema = GetDatasetValueList.model_validate(value_models)
    return schema

