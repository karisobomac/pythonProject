from user import User


class AccountInfo(User):
    def __init__(self, name, age, gender, iban):
        super().__init__(name, age, gender, iban)
        self.balance = 0

    def setBalance(self, amount):
        self.balance += amount

    def getBalance(self, ):
        return self.balance

    def view_balance(self):
        self.show_details()
        print("Account balance has been update :$", self.balance)
