from typing import Optional

from pydantic import BaseModel, Field

from models.common_model import Place


class Company(BaseModel):
    name: Optional[str] = Field(..., description="The name of the company")
    ruc: Optional[str] = Field(
        None,
        description="The RUC (Registro Único de Contribuyentes) of the company (if redacted or not available, it can be left empty)",
    )
    place: Optional[Place] = Field(
        None,
        description="The headquarters location of the company (if redacted or not available, it can be left empty)",
    )


class JobExperience(BaseModel):
    company: Optional[Company] = Field(
        ...,
        description="The company where the candidate worked",
    )
    position: Optional[str] = Field(..., description="The position held at the company")
    start_year: str = Field(
        ...,
        description="The start year of the job experience in YYYY format",
    )
    end_year: Optional[str] = Field(
        None,
        description="The end year of the job experience in YYYY format (if currently employed, it can be left empty)",
    )
