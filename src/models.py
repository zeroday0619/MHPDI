from typing import Optional
from pydantic import BaseModel
from pydantic import Field


class Address(BaseModel):
    latitude: float = Field(..., title="위도")
    longitude: float = Field(..., title="경도")
    area1: str
    area2: str
    area3: str
    distance: float

class Source(BaseModel):
    OrganizationName: str = Field(..., title="기관명")
    OrganizationType: str = Field(..., title="기관구분")
    주소: Address    
    HomePage: str = Field(..., title="홈페이지")


class ResponseModels(BaseModel):
    status: bool
    message: str | None
    source: list[Source] | None
