from datetime import datetime
from typing import Sequence, Tuple

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Result, select

from assessment.dataset.model import Dataset


class DatasetService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def __query(
        self,
        id: int | None = None,
        name: str | None = None,
        created_at: datetime | None = None,
    ) -> Result[Tuple[Dataset]]:
        stmt = select(Dataset)
        if id is not None:
            stmt = stmt.where(Dataset.id == id)
        if name is not None:
            stmt = stmt.where(Dataset.name == name)
        if created_at is not None:
            stmt = stmt.where(Dataset.created_at == created_at)
        result = await self.session.execute(stmt)
        return result

    async def one_or_none(
        self,
        id: int | None = None,
        name: str | None = None,
        created_at: datetime | None = None,
    ) -> Dataset | None:
        scalars = await self.__query(
            id=id, 
            name=name,
            created_at=created_at
        )
        return scalars.scalar_one_or_none()

    async def list(
        self,
        id: int | None = None,
        name: str | None = None,
        created_at: datetime | None = None,
    ) -> Sequence[Dataset]:
        scalars = await self.__query(
            id=id, 
            name=name, 
            created_at=created_at
        )
        return scalars.scalars().all()

    async def create(
        self, 
        name: str, 
        created_at: datetime | None = None
    ) -> Dataset:
        dataset = Dataset(name=name, created_at=created_at)
        self.session.add(dataset)
        await self.session.flush()
        return dataset

    async def delete(
        self, 
        id: int
    ) -> bool:
        result = await self.one_or_none(id=id)
        if not result:
            return False
        await self.session.delete(result)
        await self.session.flush()
        return True
