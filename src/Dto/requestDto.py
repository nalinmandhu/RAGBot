from pydantic import BaseModel

class QueryRequestDto(BaseModel):
    query: str