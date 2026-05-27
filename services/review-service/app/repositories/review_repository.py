from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.review import Review


def create_review(
    db: Session,
    review_data,
    customer_email: str
):
    review = Review(
        shop_id=review_data.shop_id,
        rating=review_data.rating,
        comment=review_data.comment,
        hygiene_rating=review_data.hygiene_rating,
        service_rating=review_data.service_rating,
        customer_email=customer_email
    )

    db.add(review)
    db.commit()
    db.refresh(review)

    return review


def get_shop_reviews(
    db: Session,
    shop_id: int
):
    return db.query(Review).filter(
        Review.shop_id == shop_id
    ).all()
    
    
def calculate_average_rating(
    db: Session,
    shop_id: int
):
    avg_rating = db.query(
        func.avg(Review.rating)
    ).filter(
        Review.shop_id == shop_id
    ).scalar()

    return round(avg_rating, 2)