from typing import TYPE_CHECKING, List
from uuid import UUID, uuid4

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .dataset import Dataset
    from .dataset_value import DatasetValue


class DatasetProduct(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    dataset_id: UUID = Field(foreign_key="dataset.id")

    dataset: "Dataset" = Relationship(back_populates="products")
    values: List["DatasetValue"] = Relationship(
        back_populates="product", cascade_delete=True
    )
