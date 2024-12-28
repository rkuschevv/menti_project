from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from src.app.services.deposit_calculator import calculate_deposit

router = APIRouter(prefix="/deposit", tags=["Deposit"])

class DepositRequest(BaseModel):
    date: str = Field("31.01.2024", pattern=r"\d{2}\.\d{2}\.\d{4}", description="Start date in format dd.mm.YYYY")
    periods: int = Field(..., ge=1, le=60, description="Number of months (1-60)")
    amount: int = Field(..., ge=10000, le=3000000, description="Initial deposit amount (10,000 to 3,000,000)")
    rate: float = Field(..., ge=1, le=8, description="Monthly interest rate (1-8%)")


@router.post("/calculate")
async def calculate_deposit_endpoint(request: DepositRequest):
    try:
        result = calculate_deposit(
            date=request.date,
            periods=request.periods,
            amount=request.amount,
            rate=request.rate
        )
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
