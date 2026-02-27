from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class DegreeLevel(str, Enum):
    BACHELOR = "bachelor"
    MASTER = "master"
    DOCTORATE = "doctorate"


class Studies(BaseModel):
    institution: str = Field(..., description="The name of the educational institution")
    degree: DegreeLevel = Field(
        ..., description="The degree level of the candidate's studies"
    )
    field: str = Field(..., description="The field of study of the candidate")
    graduation_year: Optional[int] = Field(
        ..., description="The year the candidate graduated"
    )
    notes: Optional[str] = Field(
        ..., description="Additional notes about the candidate's studies"
    )
