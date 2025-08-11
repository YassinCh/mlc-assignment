from datetime import datetime
from typing import Annotated, List

from pydantic import BaseModel, ConfigDict, RootModel, StringConstraints


class GetDataset(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: Annotated[str, StringConstraints(max_length=128)]
    created_at: datetime


class GetDatasetList(RootModel[List[GetDataset]]):
    pass
