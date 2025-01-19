from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field, validator
from datetime import datetime, date
from src.app.services.deposit_calculator import calculate_deposit
from sqlalchemy.orm import Session
from src.app.core.db import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(prefix="/deposit", tags=["Deposit"])


class DepositRequest(BaseModel):
    start_date: str = Field(..., description="Start date in format dd.mm.YYYY")
    periods: int = Field(..., ge=1, le=60, description="Number of months (1-60)")
    amount: int = Field(..., ge=10000, le=3000000, description="Initial deposit amount (10,000 to 3,000,000)")
    rate: float = Field(..., ge=1, le=8, description="Monthly interest rate (1-8%)")

    @validator("start_date")
    def validate_and_convert_date(cls, value: str) -> str:
        try:
            datetime.strptime(value, "%d.%m.%Y")  # Проверяем формат даты
            return value
        except ValueError:
            raise ValueError("Start date must be in the format dd.mm.YYYY")


@router.post("/calculate")
async def calculate_deposit_endpoint(request: DepositRequest):
    try:
        result = calculate_deposit(
            date=request.start_date,
            periods=request.periods,
            amount=request.amount,
            rate=request.rate
        )
        return {"success": True, "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail={"error": "Internal server error", "message": str(e)})
