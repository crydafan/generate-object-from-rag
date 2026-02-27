from typing import Optional
from enum import Enum

from pydantic import BaseModel, Field


class IncomeType(str, Enum):
    GROSS_ANNUAL_REMUNERATION = "gross_annual_remuneration"
    INDIVIDUAL_PROFESSIONAL_INCOME = "individual_professional_income"
    OTHER_ANNUAL_INCOME = "other_annual_income"


class IncomeBreakdown(BaseModel):
    income_type: IncomeType = Field(..., description="The type of income")
    public_sector_amount: float = Field(
        ..., description="The amount of income from the public sector"
    )
    private_sector_amount: float = Field(
        ..., description="The amount of income from the private sector"
    )
    total_amount: float = Field(..., description="The total amount of income")


class RealState(BaseModel):
    type: str = Field(..., description="The type of real estate property")
    address: str = Field(..., description="The address of the real estate property")
    value: float = Field(
        ..., description="The estimated value of the real estate property"
    )
    declared_value: float = Field(
        ...,
        description="The self-declared value of the real estate property by the candidate",
    )
    registered: bool = Field(
        ...,
        description="Indicates whether the real estate property is registered in SUNARP",
    )
    notes: Optional[str] = Field(
        ..., description="Additional notes about the real estate property"
    )


class Asset(BaseModel):
    plate: str = Field(..., description="The plate number of the vehicle")
    characteristics: str = Field(..., description="The characteristics of the vehicle")
    value: float = Field(..., description="The estimated value of the vehicle")
    notes: Optional[str] = Field(..., description="Additional notes about the vehicle")


class Shareholding(BaseModel):
    legal_entity: str = Field(..., description="The name of the legal entity")
    numer_of_shares_or_units: int = Field(
        ..., description="The number of shares or units owned"
    )
    total_nominal_value_of_shares_or_units: float = Field(
        ..., description="The total nominal value of the shares or units owned"
    )
    notes: Optional[str] = Field(
        ..., description="Additional notes about the shareholding"
    )
