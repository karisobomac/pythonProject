# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from accountInfo import AccountInfo
from transaction import Transaction
from user import User






if __name__ == '__main__':

    user1 = AccountInfo(name="burnaBoy", age=25, gender='m', iban="DE123456789101112")
    user2 = AccountInfo(name="wizkid", age=35, gender='m', iban="DE0987654321112")


    transaction = Transaction()
    transaction.deposit(500, user2)
    transaction.deposit(500, user1)

    transaction.transfer(15, user2, user1, description="payed for wallmart")
    transaction.transfer(10, user1, user2, description="payed for wallmart")
    transaction.transfer(25, user2, user1, description="payed for wallmart")
    transaction.transfer(30, user1, user2, description="payed for aldi")
    transaction.transfer(40, user2, user1, description="payed for aldi")
    transaction.transfer(60, user1, user2, description="payed for aldi")
    transaction.transfer(80, user2, user1, description="payed for aldi")
    transaction.transfer(100, user1, user2, description="cash payout")
    transaction.transfer(120, user2, user1, description="cash payout")
    transaction.transfer(140, user1, user2, description="cash payout")
    transaction.transfer(160, user2, user1, description="cash payout")
    transaction.transfer(180, user1, user2, description="salary pp")
    transaction.transfer(200, user2, user1, description="salary pp")
    transaction.transfer(220, user1, user2, description="salary pp")
    transaction.transfer(240, user2, user1, description="salary pp")


    transaction.withdrawal(4, user2, description="payed for wallmart")
    transaction.withdrawal(8, user2, description="payed for wallmart")
    transaction.withdrawal(16, user2, description="payed for wallmart")
    transaction.withdrawal(32, user2, description="payed for wallmart")
    transaction.withdrawal(64, user2, description="payed for aldi")
    transaction.withdrawal(74, user2, description="payed for aldi")
    transaction.withdrawal(84, user2, description="payed for aldi")
    transaction.withdrawal(94, user2, description="cash payout")
    transaction.withdrawal(104, user1, description="cash payout")
    transaction.withdrawal(124, user2, description="cash payout")
    transaction.withdrawal(144, user1, description="cash payout")
    transaction.withdrawal(164, user2, description="salary pp")
    transaction.withdrawal(184, user2, description="salary pp")
    transaction.withdrawal(194, user1, description="salary pp")
    transaction.withdrawal(204, user1, description="salary pp")

    for rec in transaction.getTransaction():
        print(rec)
