from app.finance_calculator import FinanceCalculator


def main():
    calc = FinanceCalculator()

    calc.add_income(10000)
    calc.add_expense(850)
    calc.add_income(500)
    calc.add_expense(300)

    print("= Finance Calculator!!!!!! =")
    print(f"Current balance: {calc.get_balance()}")


if __name__ == "__main__":
    main()
