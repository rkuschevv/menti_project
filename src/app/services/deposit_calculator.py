from datetime import datetime
from typing import Dict
import calendar


def calculate_deposit(date: str, periods: int, amount: int, rate: float) -> Dict[str, float]:
    # Преобразуем дату из строки в объект datetime
    start_date = datetime.strptime(date, "%d.%m.%Y")

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
