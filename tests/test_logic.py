from app.logic import CardValidator

def test_luhn_valid_card():
		assert CardValidator.validate_luhn("4539148408597218") is True

def test_luhn_invalid_card():
		assert CardValidator.validate_luhn("4539148408597219") is False

def test_luhn_with_spaces():
		assert CardValidator.validate_luhn("4539 1484 0859 7218") is True