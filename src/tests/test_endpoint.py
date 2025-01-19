from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

def test_calculate_deposit_endpoint():
    response = client.post(
        "/deposit/calculate",  # Правильный путь к эндпоинту
        json={
            "start_date": "31.01.2021",  # Используем корректное поле "start_date"
            "periods": 3,
            "amount": 10000,
            "rate": 5
        },
    )
    # Проверяем, что запрос выполнен успешно
    assert response.status_code == 200

    # Извлекаем данные из ответа
    response_data = response.json()

    # Проверяем структуру и значения ответа
    assert response_data["success"] is True
    assert "data" in response_data

    result = response_data["data"]
    assert result["31.01.2021"] == 10000.0
    assert result["28.02.2021"] == 10500.0
    assert result["31.03.2021"] == 11025.0
