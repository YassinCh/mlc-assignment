from datetime import datetime
from io import BytesIO
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession

from ..dataset_parser.parsers.xlsx import XlsxParser
from ..db.base_service import BaseService
from ..models.dataset import Dataset


class DatasetParserService(BaseService[Dataset]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Dataset)

    async def create_dataset_from_excel(
        self,
        bytes: BytesIO,
        dataset_name: str,
        created_at: datetime | None = None,
    ) -> Dataset:
        kwargs: dict[str, Any] = {"name": dataset_name}
        if created_at is not None:
            kwargs["created_at"] = created_at
        dataset = await self.create(**kwargs)
        xlsx_parser = XlsxParser(self.session, dataset)
        await xlsx_parser.parse(bytes)
        return dataset
