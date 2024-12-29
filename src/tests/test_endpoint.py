from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)


def test_calculate_deposit_endpoint():
    response = client.post(
        "docs#/Deposit/calculate_deposit_endpoint_deposit_calculate_post",
        json={
            "date": "31.01.2021",
            "periods": 3,
            "amount": 10000,
            "rate": 5
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert "31.01.2021" in data
    assert "28.02.2021" in data
    assert "31.03.2021" in data
    assert data["31.01.2021"] == 10000
