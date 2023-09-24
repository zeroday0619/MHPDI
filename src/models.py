from typing import Optional
from pydantic import BaseModel
from pydantic import Field


class Source(BaseModel):
    OrganizationName: str = Field(..., title="기관명")
    OrganizationType: str = Field(..., title="기관구분")
    Address: Address = Field(..., title="주소")
    HomePage: str = Field(..., title="홈페이지")


class Address(BaseModel):
    latitude: float = Field(..., title="위도")
    longitude: float = Field(..., title="경도")
    area1: str
    area2: str
    area3: str
    distance: float

class ResponseModel(BaseModel):
    status: bool
    message: Optional[str]
    source: Optional[list[Source]]
