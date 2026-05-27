import httpx


SHOP_SERVICE_URL = (
    "http://shop-service:8000"
)


def update_shop_rating(
    shop_id: int,
    rating: float
):
    url = (
        f"{SHOP_SERVICE_URL}"
        f"/api/v1/shops/{shop_id}/rating"
    )

    response = httpx.put(
        url,
        params={
            "rating": rating
        }
    )

    return response.json()