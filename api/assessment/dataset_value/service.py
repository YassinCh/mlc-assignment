from typing import Sequence, Tuple

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from assessment.dataset_value.model import DatasetValue


class DatasetValueService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def __query(
        self,
        id: int | None = None,
        product_id: int | None = None,
        feature_id: int | None = None,
    ) -> Result[Tuple[DatasetValue]]:
        stmt = select(DatasetValue)
        if id is not None:
            stmt = stmt.where(DatasetValue.id == id)
        if product_id is not None:
            stmt = stmt.where(DatasetValue.product_id == product_id)
        if feature_id is not None:
            stmt = stmt.where(DatasetValue.feature_id == feature_id)
        result = await self.session.execute(stmt)
        return result

    async def list(
        self,
        id: int | None = None,
        product_id: int | None = None,
        feature_id: int | None = None,
    ) -> Sequence[DatasetValue]:
        query = await self.__query(
            id=id, 
            product_id=product_id, 
            feature_id=feature_id
        )
        return query.scalars().all()
