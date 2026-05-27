from sqlalchemy.orm import Session

from app.models.shop import Shop


def create_shop(
    db: Session,
    shop_data,
    owner_email: str
):
    shop = Shop(
        name=shop_data.name,
        category=shop_data.category,
        address=shop_data.address,
        city=shop_data.city,
        owner_email=owner_email
    )

    db.add(shop)
    db.commit()
    db.refresh(shop)

    return shop


def get_all_shops(db: Session):
    return db.query(Shop).all()