from typing import Optional

from pydantic import BaseModel, Field


class Place(BaseModel):
    country: Optional[str] = Field(
        ..., description="The country where the place is located"
    )
    department: Optional[str] = Field(
        ..., description="The department where the place is located"
    )
    province: Optional[str] = Field(
        ..., description="The province where the place is located"
    )
    district: Optional[str] = Field(
        ..., description="The district where the place is located"
    )
    address: Optional[str] = Field(
        None,
        description="The address of the place (if redacted or not available, it can be left empty)",
    )
