from datetime import datetime
from typing import TYPE_CHECKING, List
from uuid import UUID, uuid4

from sqlalchemy import func
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .dataset_feature import DatasetFeature
    from .dataset_product import DatasetProduct


class Dataset(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(max_length=128)
    created_at: datetime = Field(default_factory=lambda: func.now())
    features: List["DatasetFeature"] = Relationship(
        back_populates="dataset", cascade_delete=True
    )
    products: List["DatasetProduct"] = Relationship(
        back_populates="dataset", cascade_delete=True
    )
