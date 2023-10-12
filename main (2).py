class BankAccount:

    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print("Deposited {}. New balance: {}".format(amount, self._account_balance))
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            print("Withdraw {}. New balance: {}".format(amount, self._account_balance))
        else:
            print("Invalid withdraw amount or insufficient balance.")

    def display_balance(self):
        print("Account balance for {} (Account #{}): {}".format(self._account_holder_name, self._account_number, self._account_balance))

# create an instance of the BankAccount class
account = BankAccount(account_number="123456789", account_holder_name="Hema", initial_balance=5000.0)

# Test deposit and withdraw functions
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.withdraw(20000.0)
account.display_balance()

