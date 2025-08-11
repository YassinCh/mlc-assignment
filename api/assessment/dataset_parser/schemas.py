from datetime import datetime
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel, ConfigDict, StringConstraints


class UploadedDataset(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: Annotated[str, StringConstraints(max_length=128)]
    created_at: datetime
