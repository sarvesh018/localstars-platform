from fastapi import FastAPI
from app.api.routes.auth import router as auth_router

from app.core.database import engine, Base
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(title="LocalStars Auth Service")

app.include_router(auth_router, prefix="/api/v1/auth")


@app.get("/health")
def health_check():
    return {"status": "healthy"}