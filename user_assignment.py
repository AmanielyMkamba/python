class User:
    bank_name = "International Bank"
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    #deposit method
    def make_deposit(self, deposited_amount):
        self.account_balance += deposited_amount
    #withdrwal method
    def make_withdrawal(self, withdrew_amount):
        self.account_balance -= withdrew_amount
    #balance display method
    def display_user_balance(self):
        print(f"User: {self.name}, Account Balance: {self.account_balance}")
    #transfer money method
    def transfer_money(self, account_balance, user):
        self.account_balance -= account_balance
        user.account_balance += account_balance
        self.display_user_balance()
        user.display_user_balance()

#first user instances
amani = User("Amani Mkamba")
amani.make_deposit(500)
amani.make_deposit(600)
amani.make_withdrawal(100)

amani.display_user_balance()

#second user instances
michael = User("Michael Baruti")
michael.make_deposit(1000)
michael.make_deposit(500)
michael.make_withdrawal(200)
michael.make_withdrawal(100)

michael.display_user_balance()


#third user instances
angel = User("Angel Gabriel")
angel.make_deposit(100)
angel.make_withdrawal(50)
angel.make_withdrawal(80)
angel.make_withdrawal(30)

angel.display_user_balance()

amani.transfer_money(100, angel)

