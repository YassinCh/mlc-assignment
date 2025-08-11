"""Query parameter models for dataset entity routes."""

from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class DatasetFeatureQueryParams(BaseModel):
    """Query parameters for dataset features endpoint."""

    dataset_id: Optional[UUID] = Field(
        None, description="Filter features by dataset ID"
    )


class DatasetProductQueryParams(BaseModel):
    """Query parameters for dataset products endpoint."""

    dataset_id: Optional[UUID] = Field(
        None, description="Filter products by dataset ID"
    )


class DatasetValueQueryParams(BaseModel):
    """Query parameters for dataset values endpoint."""

    product_id: Optional[UUID] = Field(None, description="Filter values by product ID")
    feature_id: Optional[UUID] = Field(None, description="Filter values by feature ID")
