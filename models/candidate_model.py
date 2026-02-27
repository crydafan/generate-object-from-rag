from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, computed_field, field_validator

from models.common_model import Place


class Gender(str, Enum):
    MALE = "M"
    FEMALE = "F"


class Candidate(BaseModel):
    name: str = Field(..., description="The name of the candidate")
    gender: Gender = Field(..., description="The gender of the candidate")
    birth_date: str = Field(
        ...,
        description="The birth date of the candidate in DD-MM-YYYY format",
    )

    @field_validator("birth_date", mode="before")
    def parse_birth_date(cls, value):
        if isinstance(value, str):
            return value.replace("/", "-")
        return value

    @computed_field
    @property
    def age(self) -> int:
        today = datetime.today()
        birth_date = datetime.strptime(self.birth_date, "%d-%m-%Y")
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

    birth_place: Place = Field(..., description="The birth location of the candidate")
    residence: Place = Field(
        ...,
        description="The residence location of the candidate. Default the country to Perú if not provided",
    )
