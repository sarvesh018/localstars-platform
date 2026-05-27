from fastapi import FastAPI

from app.routes.gateway_routes import router

app = FastAPI(
    title="LocalStars API Gateway"
)

app.include_router(router)


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }