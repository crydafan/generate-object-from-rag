from pydantic import BaseModel, Field


class Candidate(BaseModel):
    name: str = Field(..., description="The name of the candidate")
    age: int = Field(..., description="The age of the candidate")
    id_number: str = Field(
        ..., description="The DNI (Peruvian identity number) of the candidate"
    )
