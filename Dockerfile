# Используем базовый образ Python
FROM python:3.11-slim

# Устанавливаем зависимости для установки Poetry
RUN apt-get update && apt-get install -y curl && apt-get clean

# Устанавливаем Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Объявляем переменные окружения для Poetry
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY pyproject.toml poetry.lock ./
COPY src ./src

# Устанавливаем зависимости
RUN poetry install --no-root

# Запускаем сервер FastAPI по умолчанию
CMD ["poetry", "run", "uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
