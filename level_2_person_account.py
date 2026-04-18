#!/usr/bin/python3


class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = [] 
        self.expenses = []

    def add_income(self, amount, description):
        self.incomes.append({'amount': amount, 'description': description})
        print(f"Əlavə edildi: {amount} AZN ({description}) - Gəlir")

    def add_expense(self, amount, description):
        self.expenses.append({'amount': amount, 'description': description})
        print(f"Əlavə edildi: {amount} AZN ({description}) - Xərc")

    def total_income(self):
        total = sum(item['amount'] for item in self.incomes)
        return total

    def total_expense(self):
        total = sum(item['amount'] for item in self.expenses)
        return total

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        info = f"""
        --- {self.firstname} {self.lastname} Hesab Məlumatı ---
        Ümumi Gəlir: {self.total_income()} AZN
        Ümumi Xərc: {self.total_expense()} AZN
        Mövcud Balans: {self.account_balance()} AZN
        ----------------------------------------
        """
        return info

my_account = PersonAccount("Yusif", "Hasanli")

my_account.add_income(2000, "Maaş")
my_account.add_income(300, "Freelance layihə")
my_account.add_expense(500, "Ev kirayəsi")
my_account.add_expense(150, "Kommunal xərclər")
my_account.add_expense(400, "Qida")

print(my_account.account_info())