from typing import Sequence
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ...db.base_service import BaseService
from ...models.dataset import Dataset
from ..dependencies import get_db_session

router = APIRouter(prefix="/datasets")


@router.get("")
async def get_dataset_list(
    session: AsyncSession = Depends(get_db_session),
) -> Sequence[Dataset]:
    datasets = await BaseService(session, Dataset).list()
    return datasets


@router.get("/{id}")
async def get_dataset(
    id: UUID, session: AsyncSession = Depends(get_db_session)
) -> Dataset:
    dataset = await BaseService(session, Dataset).one_or_none(id=id)
    if not dataset:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Dataset not found")
    return dataset


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_dataset(id: UUID, session: AsyncSession = Depends(get_db_session)):
    success = await BaseService(session, Dataset).delete(id=id)
    if not success:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Dataset not found")
    await session.commit()
