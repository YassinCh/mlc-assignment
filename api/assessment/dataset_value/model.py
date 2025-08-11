from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from assessment.db.sqlalchemy import Base

if TYPE_CHECKING:
    from assessment.dataset_feature.model import DatasetFeature
    from assessment.dataset_product.model import DatasetProduct


class DatasetValue(Base):
    __tablename__ = "dataset_value"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(
        ForeignKey("dataset_product.id"), nullable=False
    )
    feature_id: Mapped[int] = mapped_column(
        ForeignKey("dataset_feature.id"), nullable=False
    )
    value: Mapped[str] = mapped_column(Text, nullable=False)

    feature: Mapped["DatasetFeature"] = relationship(back_populates="values")
    product: Mapped["DatasetProduct"] = relationship(back_populates="values")
