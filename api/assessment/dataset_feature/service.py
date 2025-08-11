from typing import Sequence, Tuple

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from assessment.dataset_feature.model import DatasetFeature


class DatasetFeatureService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def __query(
        self,
        id: int | None = None,
        dataset_id: int | None = None,
        name: str | None = None,
    ) -> Result[Tuple[DatasetFeature]]:
        stmt = select(DatasetFeature)
        if id is not None:
            stmt = stmt.where(DatasetFeature.id == id)
        if dataset_id is not None:
            stmt = stmt.where(DatasetFeature.dataset_id == dataset_id)
        if name is not None:
            stmt = stmt.where(DatasetFeature.name == name)
        result = await self.session.execute(stmt)
        return result

    async def list(
        self,
        id: int | None = None,
        dataset_id: int | None = None,
        name: str | None = None,
    ) -> Sequence[DatasetFeature]:
        query = await self.__query(
            id=id, 
            dataset_id=dataset_id,
            name=name
        )
        return query.scalars().all()
