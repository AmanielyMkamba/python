class BankAccount:
    bank_name = "International Bank"
    accounts = []
    def __init__ (self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    # deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        return self

    # withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdrawal(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    # display_account_info(self) - print to the console: eg. "Balance: $100"
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    # yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if(self.balance >= 0):
            self.balance +=self.balance*self.int_rate
        return self

    # NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

#first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
checking_account = BankAccount(0.07)
checking_account.deposit(500).deposit(300).deposit(200).withdrawal(100).yield_interest().display_account_info()

#second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
savings_account = BankAccount(0.05, 250)
savings_account.deposit(200).deposit(100).withdrawal(200).withdrawal(50).withdrawal(150).withdrawal(400).withdrawal(300).yield_interest().display_account_info()

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
BankAccount.print_all_accounts()


