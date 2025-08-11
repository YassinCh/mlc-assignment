from typing import List

from pydantic import BaseModel, ConfigDict, RootModel


class GetDatasetValue(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    product_id: int
    feature_id: int
    value: str


class GetDatasetValueList(RootModel[List[GetDatasetValue]]):
    pass
