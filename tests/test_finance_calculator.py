import pytest
from app.finance_calculator import MortgageCalculator

def test_calculate_monthly_payment():
    calc = MortgageCalculator()
    calc.set_credit(1_000_000)
    calc.set_rate(10)
    calc.set_years(10)
    result = calc.calculate_monthly_payment()
    assert result == 9166.67  # <-- можешь потом поменять это число, чтобы тест "упал"

def test_invalid_values():
    calc = MortgageCalculator()
    calc.set_credit(-1000)
    calc.set_rate(10)
    calc.set_years(10)
    with pytest.raises(ValueError):
        calc.calculate_monthly_payment()
