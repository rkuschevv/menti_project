# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y curl && apt-get clean

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Устанавливаем Poetry
RUN pip install poetry

# Устанавливаем зависимости проекта
RUN poetry config virtualenvs.create false && poetry install --no-root

# Открываем порт для приложения
EXPOSE 8000

# Команда для запуска
CMD ["poetry", "run", "uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
