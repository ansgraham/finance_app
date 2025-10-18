from finance_calculator import MortgageCalculator

def main():
    calc = MortgageCalculator()
    calc.set_credit(1_000_000)
    calc.set_rate(10)
    calc.set_years(10)
    monthly = calc.calculate_monthly_payment()
    print("Ежемесячный платёж:", monthly)
    print(calc.get_summary())

if __name__ == "__main__":
    main()
