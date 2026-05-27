from pydantic import BaseModel


class ReviewCreate(BaseModel):
    shop_id: int
    rating: float
    comment: str
    hygiene_rating: float
    service_rating: float