from Bank_system import Bank_System


class Bank_Account(Bank_System):

    def __init__(
        self,
        user_name,
        bank_name,
        password,
        balance: 0.0,
        file_users="Names.csv",
    ):
        super().__init__(file_users)
        try:
            self.balance = float(balance)
        except (ValueError, TypeError):
            self.balance = 0.0

        if self.balance < 0:
            raise ValueError("Balance cannot be negative")
        self.user_name = user_name
        self.bank_name = bank_name
        self.__password = password
        self.balance = float(balance)

    def check_password(self, enterd_password):
        return self.__password == enterd_password

    def get_password(self):
        return self.__password

    def show_information(self):
        print("Account Information:\n")
        print(f"User Name: {self.user_name}\n")
        print(f"Bank Name: {self.bank_name}\n")
        print(f"Balance: {self.balance} EGB\n")

    def deposit(self, amount: float):
        """Deposit a Money to the account"""
        if amount > 0:
            self.balance += amount
            print(f"Deposit Added {amount}, Your new balance is: {self.balance} EGB\n")

        else:
            raise ValueError("Deposit amount must be positive")

    def withdrawl(self, amount: float):
        """withdrawl a Money from the account"""
        if amount > self.balance:
            raise ValueError("the amount is bigger than the balance")
        if amount <= 0:
            raise ValueError("the amount must be positive")
        else:
            self.balance -= amount
            print(f"withdrawal {amount}, Your balance now is: {self.balance} EGB\n")
