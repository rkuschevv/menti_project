from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

def test_calculate_endpoint():
    response = client.post("/deposit/calculate", json={
        "date": "01.01.2021",
        "periods": 3,
        "amount": 10000,
        "rate": 1
    })
    assert response.status_code == 200
    assert response.json() == {
        "31.01.2021": 10100.0,
        "28.02.2021": 10201.0,
        "31.03.2021": 10201.0
    }
