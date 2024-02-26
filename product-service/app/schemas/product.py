import uuid
import datetime
from app.schemas.base import BaseModel

class Product(BaseModel):
    name: str
    description: str
    price: float
    category: str
    tags: str
    brand: str
    availability: bool

class ProductResponse(Product):
    uuid: uuid.UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime

class ProductInput(Product):
    pass

