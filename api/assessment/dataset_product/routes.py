from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from assessment.dataset_product.schemas import GetDatasetProductList
from assessment.dataset_product.service import DatasetProductService
from assessment.api.fastapi.dependencies import get_db_session

router = APIRouter(prefix="/dataset_products")


@router.get("")
async def get_dataset_product_list(
    dataset_id: Optional[int] = None, session: AsyncSession = Depends(get_db_session)
):
    service = DatasetProductService(session)
    product_list = await service.list(dataset_id=dataset_id)
    if not product_list:
        raise HTTPException(status_code=404, detail="No dataset products found")
    schema = GetDatasetProductList.model_validate(product_list)
    return schema