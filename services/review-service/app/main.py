from fastapi import FastAPI

from app.core.database import (
    engine,
    Base
)

from app.models.review import Review

from app.api.routes.reviews import (
    router as review_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LocalStars Review Service"
)

app.include_router(
    review_router,
    prefix="/api/v1/reviews"
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}