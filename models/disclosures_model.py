from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class DisclosureType(str, Enum):
    LABOR = "labor"
    FAMILY_SUPPORT = "family_support"
    CONTRACTUAL = "contractual"
    DOMESTIC_VIOLENCE = "domestic_violence"


class Disclosure(BaseModel):
    type: DisclosureType = Field(..., description="The type of disclosure")
    case: str = Field(
        ..., description="The case number or identifier associated with the disclosure"
    )
    ruling: str = Field(
        ..., description="The ruling or decision made in relation to the disclosure"
    )
    notes: Optional[str] = Field(
        None,
        description="Additional notes or details about the disclosure",
    )
