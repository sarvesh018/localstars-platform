from fastapi import FastAPI

from app.core.database import (
    engine,
    Base
)

from app.models.shop import Shop

from app.api.routes.shops import (
    router as shop_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LocalStars Shop Service"
)

app.include_router(
    shop_router,
    prefix="/api/v1/shops"
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}