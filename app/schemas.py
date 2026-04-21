from pydantic import BaseModel, Field
from enum import Enum
from typing import Optional

class TransactionType(str, Enum):
		DEBIT = "debit"
		CREDIT = "credit"

class Transaction(BaseModel):
		amount: float = Field(gt=0, description="Сумма транзакций должна быть положительной")
		type: TransactionType
		card_number:  str = Field(min_length=13, max_length=19)
		description: Optional[str] = Field(None, max_length=100)

