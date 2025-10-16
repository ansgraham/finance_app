class FinanceCalculator:
    def __init__(self):
        self.transactions = []

    def add_income(self, amount):
        if amount <= 0:
            raise ValueError("=Доход должен быть положительным числом")
        self.transactions.append(("income", amount))

    def add_expense(self, amount):
        if amount <= 0:
            raise ValueError("=Расход должен быть положительным числом")
        self.transactions.append(("expense", amount))

    def get_balance(self):
        income = sum(a for t, a in self.transactions if t == "income")
        expense = sum(a for t, a in self.transactions if t == "expense")
        return income - expense
