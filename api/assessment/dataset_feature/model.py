from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from assessment.db.sqlalchemy import Base

if TYPE_CHECKING:
    from assessment.dataset.model import Dataset
    from assessment.dataset_value.model import DatasetValue


class DatasetFeature(Base):
    __tablename__ = "dataset_feature"

    id: Mapped[int] = mapped_column(primary_key=True)
    dataset_id: Mapped[int] = mapped_column(ForeignKey("dataset.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)

    dataset: Mapped["Dataset"] = relationship(back_populates="features")
    values: Mapped[List["DatasetValue"]] = relationship(back_populates="feature", cascade="all, delete-orphan")
