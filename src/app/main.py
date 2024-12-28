from fastapi import FastAPI
from src.app.routers import deposit

app = FastAPI(
    title="Deposit Calculator API",
    description="API for calculating deposit amounts based on input parameters",
    version="1.0.0"
)

# Подключение роутеров
app.include_router(deposit.router)