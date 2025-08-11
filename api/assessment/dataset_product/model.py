from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from assessment.db.sqlalchemy import Base

if TYPE_CHECKING:
    from assessment.dataset.model import Dataset
    from assessment.dataset_value.model import DatasetValue


class DatasetProduct(Base):
    __tablename__ = "dataset_product"

    id: Mapped[int] = mapped_column(primary_key=True)
    dataset_id: Mapped[int] = mapped_column(ForeignKey("dataset.id"), nullable=False)

    dataset: Mapped["Dataset"] = relationship(back_populates="products")
    values: Mapped[List["DatasetValue"]] = relationship(back_populates="product", cascade="all, delete-orphan")
