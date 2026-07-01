from fastapi import APIRouter, Query
from fastapi.testclient import TestClient


def test_validation_error_shape(client: TestClient) -> None:
    app = client.app
    router = APIRouter()

    @router.get("/api/v1/test-validation")
    async def test_validation(value: int = Query(...)) -> dict[str, int]:
        return {"value": value}

    app.include_router(router)

    response = client.get("/api/v1/test-validation?value=abc")
    assert response.status_code == 422
    body = response.json()
    assert "error" in body
    assert body["error"]["code"] == "VALIDATION_ERROR"
    assert "details" in body["error"]
