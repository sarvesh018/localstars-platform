from sqlalchemy import (
    Column,
    Integer,
    String,
    Float
)

from app.core.database import Base


class Shop(Base):
    __tablename__ = "shops"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    category = Column(String, nullable=False)

    address = Column(String, nullable=False)

    city = Column(String, nullable=False)

    rating = Column(Float, default=0)

    owner_email = Column(
        String,
        nullable=False
    )