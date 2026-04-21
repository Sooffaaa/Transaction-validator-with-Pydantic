from fastapi import FastAPI, HTTPException
from typing import List
from .schemas import Transaction
from .logic import CardValidator

app = FastAPI()

@app.post("/validate")
async def validate_transactions(transactions: List[Transaction]):
		valid_transactions_gen = (
        tx for tx in transactions 
        if CardValidator.validate_luhn(tx.card_number)
		)

		result = list(valid_transactions_gen)

		if not result:
				raise HTTPException(
					status_code=400,
					detail="Ни одна транзакция не прошла валидацию номера карты"
				)

		return {
			"status": "success",
			"valid_count": len(result),
			"total_processed": len(transactions),
			"data": result
		}
