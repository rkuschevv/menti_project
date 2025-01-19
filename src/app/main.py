from fastapi import FastAPI
from src.app.routers import deposit

app = FastAPI()

# Подключение роутеров
app.include_router(deposit.router)