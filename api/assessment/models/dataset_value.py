from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .dataset_feature import DatasetFeature
    from .dataset_product import DatasetProduct


class DatasetValue(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    product_id: UUID = Field(foreign_key="datasetproduct.id")
    feature_id: UUID = Field(foreign_key="datasetfeature.id")
    value: str

    feature: "DatasetFeature" = Relationship(back_populates="values")
    product: "DatasetProduct" = Relationship(back_populates="values")
