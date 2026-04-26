# 📈 Валидатор транзакций с Pydantic (FastAPI + Binance API)

Система фильтрации финансовых переводов. Главная задача — отсеять опечатки в номерах карт и ошибки в суммах.

## 🛠 Стек технологий
* FastAPI, Pydantic, pytest
   
## 📈 Пример работы API
Эндпоинт: POST /validate
Вход (Request Body):

[
  {
    "amount": 100.0,
    "type": "credit",
    "card_number": "4539148408597218"
  },
  {
    "amount": 50.0,
    "type": "debit",
    "card_number": "4539148408597219" 
  }
]

Выход (Response):
Система вернет только первую транзакцию, так как вторая не пройдет проверку алгоритмом Луна.

{
  "status": "success",
  "valid_count": 1,
  "total_processed": 2,
  "data": [
		{
			"amount": 100.0,
			"type": "credit",
			"card_number": "4539148408597218"
  	}
	]
}
