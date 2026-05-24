from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import UserRegister
from app.core.database import get_db
from app.core.security import hash_password

from app.repositories.user_repository import (
    get_user_by_email,
    create_user
)

router = APIRouter()


@router.post("/register")
def register_user(
    user: UserRegister,
    db: Session = Depends(get_db)
):
    existing_user = get_user_by_email(db, user.email)

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    hashed_password = hash_password(user.password)

    new_user = create_user(
        db=db,
        name=user.name,
        email=user.email,
        password=hashed_password
    )

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }


@router.post("/login")
def login_user():
    return {
        "message": "User login successful"
    }