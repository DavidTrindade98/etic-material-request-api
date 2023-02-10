from pydantic import BaseModel, validator
from datetime import datetime

class PublicRequestsAPI(BaseModel):
    id: int
    school_class: str
    requester: str
    start_datetime: datetime
    end_datetime: datetime
    subject: str
    context: str
    observations: str

class UpdateRequest(BaseModel):
    requester: str
    end_datetime: datetime
    subject: str
    observations: str  

class PublicInventoryGroupAPI(BaseModel):

    id: int
    name: str

class PublicInventoryCategoryAPI(BaseModel):

    id: int
    group_id: int
    name: str

class PublicInventoryAPI(BaseModel):

    id: int
    name: str
    category: int
    sku: int

class PublicRequestsInventory(BaseModel):

    request_id: int
    material_requested_id: int
    requested: datetime
    delivered: datetime