import traceback
from io import BytesIO

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from ...dataset_parser.schemas import UploadedDataset
from ...dataset_parser.service import DatasetParserService
from ..dependencies import get_db_session

router = APIRouter(prefix="/dataset_parsers")


@router.post("/excel", status_code=201)
async def upload_dataset(
    dataset_name: str = Form(...),
    excel_file: UploadFile = File(...),
    session: AsyncSession = Depends(get_db_session),
) -> UploadedDataset:
    if (
        excel_file.content_type
        != "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    ):
        raise HTTPException(status_code=415, detail="Not a xlsx file")

    contents = await excel_file.read()
    buffer = BytesIO(contents)
    dataset_service = DatasetParserService(session)
    dataset = None
    try:
        dataset = await dataset_service.create_dataset_from_excel(
            bytes=buffer, dataset_name=dataset_name
        )
        await session.commit()
    except Exception:
        traceback.print_exc()
        await session.rollback()
        raise HTTPException(status_code=500, detail="Error during dataset creation")

    buffer.close()

    schema = UploadedDataset.model_validate(dataset)
    return schema
