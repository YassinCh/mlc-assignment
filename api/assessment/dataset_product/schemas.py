from typing import List

from pydantic import BaseModel, ConfigDict, RootModel


class GetDatasetProduct(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int


class GetDatasetProductList(RootModel[List[GetDatasetProduct]]):
    pass
