from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.core.dependencies import get_current_user
from app.models.user import User
from app.core.security import (
    verify_password,
    create_access_token
)
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
        password=hashed_password,
        role=user.role
    )

    return {
        "message": "User registered successfully",
        "user_id": new_user.id
    }


@router.post("/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = get_user_by_email(
        db,
        form_data.username
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    is_valid_password = verify_password(
        form_data.password,
        user.password
    )

    if not is_valid_password:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={
            "sub": user.email,
            "role": user.role
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
    
@router.get("/me")
def get_logged_in_user(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "role": current_user.role
    }