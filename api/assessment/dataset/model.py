from datetime import datetime
from typing import TYPE_CHECKING, List

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from assessment.db.sqlalchemy import Base

if TYPE_CHECKING:
    from assessment.dataset_feature.model import DatasetFeature
    from assessment.dataset_product.model import DatasetProduct


class Dataset(Base):
    __tablename__ = "dataset"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), nullable=False)
                 
    features: Mapped[List["DatasetFeature"]] = relationship(back_populates="dataset", cascade="all, delete-orphan")
    products: Mapped[List["DatasetProduct"]] = relationship(back_populates="dataset", cascade="all, delete-orphan")
