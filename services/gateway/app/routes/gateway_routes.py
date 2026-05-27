from fastapi import (
    APIRouter,
    Request
)

from fastapi.responses import JSONResponse

import httpx
import os

from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

AUTH_SERVICE_URL = os.getenv(
    "AUTH_SERVICE_URL"
)

SHOP_SERVICE_URL = os.getenv(
    "SHOP_SERVICE_URL"
)

REVIEW_SERVICE_URL = os.getenv(
    "REVIEW_SERVICE_URL"
)


@router.api_route(
    "/auth/{path:path}",
    methods=["GET", "POST", "PUT", "DELETE"]
)
async def auth_proxy(
    path: str,
    request: Request
):
    async with httpx.AsyncClient() as client:

        url = (
            f"{AUTH_SERVICE_URL}"
            f"/api/v1/auth/{path}"
        )

        response = await client.request(
            method=request.method,
            url=url,
            headers=request.headers.raw,
            content=await request.body()
        )

        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )


@router.api_route(
    "/shops/{path:path}",
    methods=["GET", "POST", "PUT", "DELETE"]
)
async def shop_proxy(
    path: str,
    request: Request
):
    async with httpx.AsyncClient() as client:

        url = (
            f"{SHOP_SERVICE_URL}"
            f"/api/v1/shops/{path}"
        )

        response = await client.request(
            method=request.method,
            url=url,
            headers=request.headers.raw,
            content=await request.body(),
            params=request.query_params
        )

        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )


@router.api_route(
    "/reviews/{path:path}",
    methods=["GET", "POST", "PUT", "DELETE"]
)
async def review_proxy(
    path: str,
    request: Request
):
    async with httpx.AsyncClient() as client:

        url = (
            f"{REVIEW_SERVICE_URL}"
            f"/api/v1/reviews/{path}"
        )

        response = await client.request(
            method=request.method,
            url=url,
            headers=request.headers.raw,
            content=await request.body(),
            params=request.query_params
        )

        return JSONResponse(
            status_code=response.status_code,
            content=response.json()
        )