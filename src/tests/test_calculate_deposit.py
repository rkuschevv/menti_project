import pytest
from src.app.services.deposit_calculator import calculate_deposit


def test_calculate_deposit_valid():
    result = calculate_deposit(
        date="01.01.2021",
        periods=3,
        amount=10000,
        rate=1
    )
    expected = {
        "01.01.2021": 10000.0,
        "28.02.2021": 10100.0,
        "31.03.2021": 10201.0
    }
    assert result == expected


def test_calculate_deposit_invalid_date():
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_deposit(
            date="invalid_date",
            periods=3,
            amount=10000,
            rate=1
        )


def test_calculate_deposit():
    result = calculate_deposit(
        date="31.01.2021",
        periods=3,
        amount=10000,
        rate=5,
    )
    assert len(result) == 3
    assert result["31.01.2021"] == 10000
    assert result["28.02.2021"] == 10500
    assert result["31.03.2021"] == 11025
