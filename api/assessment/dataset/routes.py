from assessment.dataset.schemas import GetDataset, GetDatasetList
from assessment.dataset.service import DatasetService

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from assessment.api.fastapi.dependencies import get_db_session

router = APIRouter(prefix="/datasets")


@router.get("")
async def get_dataset_list(
    session: AsyncSession = Depends(get_db_session),
) -> GetDatasetList:
    dataset_service = DatasetService(session)
    datasets = await dataset_service.list()
    schema = GetDatasetList.model_validate(datasets)
    return schema


@router.get("/{id}")
async def get_dataset(
    id: int, session: AsyncSession = Depends(get_db_session)
) -> GetDataset:
    dataset_service = DatasetService(session)
    dataset = await dataset_service.one_or_none(id=id)
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")
    schema = GetDataset.model_validate(dataset)
    return schema


@router.delete("/{id}", status_code=204)
async def delete_dataset(id: int, session: AsyncSession = Depends(get_db_session)):
    dataset_service = DatasetService(session)
    success = await dataset_service.delete(id=id)
    if not success:
        raise HTTPException(status_code=404, detail="Dataset not found")
    await session.commit()

