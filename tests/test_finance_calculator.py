import pytest
from app.finance_calculator import FinanceCalculator


def test_add_income_and_expense():
    calc = FinanceCalculator()
    calc.add_income(1000)
    calc.add_expense(400)
    assert calc.get_balance() == 600


def test_negative_income_raises_error():
    calc = FinanceCalculator()
    with pytest.raises(ValueError):
        calc.add_income(-100)


def test_negative_expense_raises_error():
    calc = FinanceCalculator()
    with pytest.raises(ValueError):
        calc.add_expense(-50)
