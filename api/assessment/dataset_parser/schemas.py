from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, StringConstraints


class UploadedDataset(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: Annotated[str, StringConstraints(max_length=128)]
    created_at: datetime
