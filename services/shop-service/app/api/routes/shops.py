from fastapi import (
    APIRouter,
    Depends
)
from sqlalchemy.orm import Session
from app.repositories.shop_repository import (
    update_shop_rating
)
from app.schemas.shop import ShopCreate
from app.core.database import get_db
from app.core.dependencies import (
    get_current_user
)
from app.repositories.shop_repository import (
    create_shop,
    get_all_shops
)

router = APIRouter()


@router.post("/")
def create_new_shop(
    shop: ShopCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    new_shop = create_shop(
        db=db,
        shop_data=shop,
        owner_email=current_user["email"]
    )

    return {
        "message": "Shop created successfully",
        "shop_id": new_shop.id
    }


@router.get("/")
def get_shops(
    db: Session = Depends(get_db)
):
    shops = get_all_shops(db)

    return shops

@router.put("/{shop_id}/rating")
def update_rating(
    shop_id: int,
    rating: float,
    db: Session = Depends(get_db)
):
    updated_shop = update_shop_rating(
        db,
        shop_id,
        rating
    )

    if not updated_shop:
        return {
            "message": "Shop not found"
        }

    return {
        "message": "Shop rating updated",
        "rating": updated_shop.rating
    }