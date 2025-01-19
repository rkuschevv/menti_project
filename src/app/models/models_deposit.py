from sqlalchemy import Column, Integer, String, Float, Date
from src.app.core.db import Base

class Deposit(Base):
    __tablename__ = "deposits"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(Date, nullable=False)
    periods = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    rate = Column(Float, nullable=False)
    result = Column(String, nullable=False)  # Результаты в виде JSON-строки
