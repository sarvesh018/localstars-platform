from pydantic import BaseModel


class ShopCreate(BaseModel):
    name: str
    category: str
    address: str
    city: str