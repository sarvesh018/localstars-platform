from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse

from app.services.qr_service import (
    generate_qr
)
from app.schemas.review import ReviewCreate

from app.core.database import get_db

from app.core.dependencies import (
    get_current_user
)

from app.repositories.review_repository import (
    create_review,
    get_shop_reviews
)
from app.repositories.review_repository import (
    calculate_average_rating
)

from app.services.rating_service import (
    update_shop_rating
)
router = APIRouter()


@router.post("/")
def create_new_review(
    review: ReviewCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    new_review = create_review(
        db=db,
        review_data=review,
        customer_email=current_user["email"]
    )

    average_rating = calculate_average_rating(
        db,
        review.shop_id
    )

    update_shop_rating(
        review.shop_id,
        average_rating
    )

    return {
        "message": "Review added successfully",
        "review_id": new_review.id,
        "average_rating": average_rating
    }


@router.get("/{shop_id}")
def get_reviews(
    shop_id: int,
    db: Session = Depends(get_db)
):
    reviews = get_shop_reviews(
        db,
        shop_id
    )

    return reviews

@router.get("/qr/{shop_id}")
def generate_shop_qr(shop_id: int):

    file_path = generate_qr(shop_id)

    return FileResponse(
        path=file_path,
        media_type="image/png",
        filename=f"shop_{shop_id}.png"
    )