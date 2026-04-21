class CardValidator:
    @staticmethod
    def validate_luhn(card_number: str) -> bool:
        card_number = card_number.replace(" ", "")
        if not card_number.isdigit():
            return False

        digits = [int(d) for d in card_number]
        checksum = 0
        reverse_digits = digits[::-1]
        
        # print(f"\n--- Отладка карты: {card_number} ---")
        
        for i, digit in enumerate(reverse_digits):
            original_digit = digit
            
            if i % 2 == 1:
                digit *= 2
                if digit > 9:
                    digit -= 9
            
            checksum += digit
            # print(f"Позиция: {i} | Было: {original_digit} -> Стало: {digit} | Сумма: {checksum}")
            
        is_valid = checksum % 10 == 0
        # print(f"ИТОГ: Сумма {checksum} делится на 10? -> {is_valid}")
        return is_valid
