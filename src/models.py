from pydantic import BaseModel
from pydantic import Field


class AddressModel(BaseModel):
    latitude: float = Field(..., alias="위도")
    longitude: float = Field(..., alias="경도")
    area1: str
    area2: str
    area3: str
    distance: float

class DataModel(BaseModel):
    OrganizationName: str = Field(..., alias="기관명")
    OrganizationType: str = Field(..., alias="기관구분")
    Address: AddressModel = Field(..., alias="주소")    
    HomePage: str = Field(..., alias="홈페이지")

class ReverseGeoAddressModel(BaseModel):
    area1: str
    area2: str
    area3: str
    
class SourceModel(BaseModel):
    address: ReverseGeoAddressModel
    data: list[DataModel]

class ResponseModel(BaseModel):
    status: bool
    message: str | None
    source: SourceModel | None
