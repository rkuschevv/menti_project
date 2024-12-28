from datetime import datetime
from typing import Dict
import calendar

def calculate_deposit(date: str, periods: int, amount: int, rate: float) -> Dict[str, float]:
    if date is None:
        start_date = datetime.now()
    else:
        try:
            start_date = datetime.strptime(date, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use dd.mm.YYYY.")

    if not (1 <= periods <= 60):
        raise ValueError("Periods must be between 1 and 60.")

    if not (10000 <= amount <= 3000000):
        raise ValueError("Amount must be between 10,000 and 3,000,000.")

    if not (1 <= rate <= 8):
        raise ValueError("Rate must be between 1 and 8.")

    monthly_rate = rate / 100
    results = {}
    current_date = start_date
    current_amount = amount

    for _ in range(periods):
        results[current_date.strftime("%d.%m.%Y")] = round(current_amount, 2)
        current_amount += current_amount * monthly_rate

        # Определяем следующий месяц и год
        next_month = current_date.month + 1
        year = current_date.year + (next_month - 1) // 12
        month = (next_month - 1) % 12 + 1

        # Устанавливаем день в последний день следующего месяца
        last_day = calendar.monthrange(year, month)[1]
        current_date = current_date.replace(year=year, month=month, day=last_day)

    return results
