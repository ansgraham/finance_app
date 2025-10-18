class MortgageCalculator:
    def __init__(self):
        self.credit_sum = 0
        self.rate = 0
        self.years = 0
        self.monthly_payment = 0

    def set_credit(self, amount: float):
        self.credit_sum = amount

    def set_rate(self, percent: float):
        self.rate = percent

    def set_years(self, years: int):
        self.years = years

    def calculate_monthly_payment(self):
        if self.credit_sum <= 0 or self.rate <= 0 or self.years <= 0:
            raise ValueError("Все значения должны быть положительными!")

        self.monthly_payment = round(
            (self.credit_sum * (1 + self.rate / 100)) / (self.years * 12),
            2,
        )
        return self.monthly_payment

    def get_summary(self):
        return (
            f"Кредит: {self.credit_sum}₽, "
            f"ставка: {self.rate}%, "
            f"срок: {self.years} лет, "
            f"платёж: {self.monthly_payment}₽"
        )
