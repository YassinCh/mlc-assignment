from typing import Sequence, Tuple

from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from assessment.dataset_product.model import DatasetProduct


class DatasetProductService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def __query(
        self,
        id: int | None = None,
        dataset_id: int | None = None,
    ) -> Result[Tuple[DatasetProduct]]:
        stmt = select(DatasetProduct)
        if id is not None:
            stmt = stmt.where(DatasetProduct.id == id)
        if dataset_id is not None:
            stmt = stmt.where(DatasetProduct.dataset_id == dataset_id)
        result = await self.session.execute(stmt)
        return result

    async def list(
        self,
        id: int | None = None,
        dataset_id: int | None = None,
    ) -> Sequence[DatasetProduct]:
        query = await self.__query(
            id=id, 
            dataset_id=dataset_id,
        )
        return query.scalars().all()


