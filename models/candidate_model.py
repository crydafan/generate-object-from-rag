from pydantic import BaseModel, Field


class Candidate(BaseModel):
    name: str = Field(..., description="The name of the candidate")
    birth_date: str = Field(
        ..., description="The birth date of the candidate in DD-MM-YYYY format"
    )
    id_number: str = Field(
        ..., description="The DNI (Peruvian identity number) of the candidate"
    )
