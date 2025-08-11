from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from assessment.dataset_feature.schemas import GetFeatureList
from assessment.api.fastapi.dependencies import get_db_session
from assessment.dataset_feature.service import DatasetFeatureService

router = APIRouter(prefix="/dataset_features")


@router.get("")
async def get_dataset_features_list(
    dataset_id: Optional[int] = None, session: AsyncSession = Depends(get_db_session)
):
    service = DatasetFeatureService(session)
    feature_models = await service.list(dataset_id=dataset_id)
    if not feature_models:
        raise HTTPException(status_code=404, detail="No features found")
    schema = GetFeatureList.model_validate(feature_models)
    return schema
