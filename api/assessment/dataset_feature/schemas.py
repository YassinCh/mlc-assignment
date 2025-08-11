from typing import List, Optional

from pydantic import BaseModel, ConfigDict, RootModel


class GetFeature(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    dataset_id: int
    name: str


class GetFeatureList(RootModel[List[GetFeature]]):
    pass
