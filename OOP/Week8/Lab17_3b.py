class BankAccount(object):
    def __init__(self, name="", last_name="", address="", iban="", account_number=0, balance=0):
        self.__name = name
        self.__last_name = last_name
        self.__address = address
        self.__iban = iban
        self.__account_number = account_number
        self.__balance = balance
        self.__transactions = {}  # Dictionary to store all transactions. The key is the id of the transaction
        # The value is a tuple (a, b, c, d) where a is the value being deposited or
        # withdrawn, b is the type of transaction (deposit or withdraw), c is the balance after the transaction, and d
        # is a message the user can attached with the transaction
        # An example of 3 transactions from a initial balance of 100 could be:
        #  {1:(100, "deposit", 200, "salary"), 2:(55.60, "withdraw", 144.4, "electricity"), 3:(34, "withdraw", 110.4, "phone bill")}

        self.__transactions_count = 0  # A counter that needs to be incremented by 1 for each deposit or withdraw and
        # that is also used to identify a transaction

    def deposit(self, value, message):
        if value < 0:
            print("You cannot deposit a negative value")

        try:
            value = float(value)
        except ValueError:
            print("Value is not a number. Please pass a correct deposit value")
            return

        self.__balance += value
        self.__transactions_count += 1
        self.__transactions.update({self.__transactions_count: (value, "deposit", self.__balance, message)})

    def withdraw(self, value, message):
        if value < 0:
            print("You cannot withdraw a negative value")

        try:
            value = float(value)
        except ValueError:
            print("Value is not a number. Please pass a correct withdraw value")
            return

        if value > self.__balance:
            print("Value to withdraw greater than current balance. Operation cannnot be concluded")
            return

        self.__balance -= value
        self.__transactions_count += 1
        self.__transactions.update({self.__transactions_count: (value, "withdraw", self.__balance, message)})

    def print_last_five_transactions(self):
        count = self.__transactions_count

        if count == 0:
            print("No transactions have been performed yet\n")
            return

        count_printed = 0
        while count > 0:
            count_printed += 1
            for key, value in self.__transactions.items():
                if key == count:
                    print("Transaction type:", value[1])
                    print("Value:", value[0])
                    print("Message:", value[3])
                    print("Balance:", value[2])
                    print()
                    break
            if count_printed == 5:
                break
            count -= 1

    def print_balance(self):
        print("Your current balance is", self.__balance)


# Lucas account with lots of money
lucas_account = BankAccount(name="Lucas", last_name="Rizzo", address="TUD", iban="IE12345789", balance=1000000)
lucas_account.print_last_five_transactions()

# Deposit from some profit with bitcoin
lucas_account.deposit(500000, "bitcoin profit")
lucas_account.withdraw(750000, "casino bet")
lucas_account.withdraw(200000, "trip to bahamas")
lucas_account.withdraw(200000, "money to lawyers")
lucas_account.withdraw(350000, "money to hideout")
lucas_account.print_last_five_transactions()





