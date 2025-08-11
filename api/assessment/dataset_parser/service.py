from datetime import datetime
from io import BytesIO

from sqlalchemy.ext.asyncio import AsyncSession

from assessment.dataset.model import Dataset
from assessment.dataset.service import DatasetService
from assessment.dataset_parser.parsers.xlsx import XlsxParser


class DatasetParserService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_dataset_from_excel(
        self,
        bytes: BytesIO,
        dataset_name: str,
        created_at: datetime | None = None,
    ) -> Dataset:
        dataset_service = DatasetService(self.session)
        dataset = await dataset_service.create(dataset_name, created_at)
        xlsx_parser = XlsxParser(self.session, dataset)
        await xlsx_parser.parse(bytes)
        return dataset
