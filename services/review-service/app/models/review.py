from sqlalchemy import (
    Column,
    Integer,
    String,
    Float
)

from app.core.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)

    shop_id = Column(Integer, nullable=False)

    customer_email = Column(
        String,
        nullable=False
    )

    rating = Column(Float, nullable=False)

    comment = Column(String)

    hygiene_rating = Column(Float)

    service_rating = Column(Float)