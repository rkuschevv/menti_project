from fastapi import FastAPI
from src.app.routers import deposit

app = FastAPI()

# Define your routes here

# Подключение роутеров
app.include_router(deposit.router)