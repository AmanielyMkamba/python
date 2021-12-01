class BankAccount:
    # declaring class attributes
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    # deposit method
    def deposit(self, amount):
        self.balance += amount
        return self

    # withdraw method
    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    # display account info method
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    # interest yield method
    def yield_interest(self):
        if(self.balance >= 0):
            self.balance +=self.balance*self.int_rate
        return self

# ..................//........................//.................................//...........................

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}")
        self.account.display_account_info()
        return self

    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdraw(amount)
        return self

# intances
amani = User("Amani Mkamba", "amani.mkamba@gmail.com").make_deposit(100).make_deposit(200).make_deposit(300).make_withdraw(150)
amani.account.yield_interest()
amani.display_user_balance()

sheena = User("Sheena She", "sheena_she@gmail.com").make_deposit(100).make_deposit(200).make_deposit(300).make_withdraw(1500)
sheena.account.yield_interest()
sheena.display_user_balance()

amani.transfer_money(sheena, 200).display_user_balance()
sheena.display_user_balance()
