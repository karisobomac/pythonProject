import hashlib
import json


class Transaction:
    transaction = list()
    amount = 0
    data = dict()
    transactionCode = None

    def getTransactioncode(self, data):
        md5_hash = hashlib.md5()

        content = data
        md5_hash.update(content)
        digest = md5_hash.hexdigest()
        print(digest)
        return digest

    def deposit(self, amount, accountOwner, description=None):
        if amount > 0:
            accountOwner.setBalance(amount)
            self.recTransaction(accountOwner, accountOwner, "Successful", amount, label=description)
        else:
            self.recTransaction(accountOwner, accountOwner, "Unsuccessful", amount, label=description)

    def transfer(self, amount, sender, receiver, description=None):
        print(sender)
        if 0 < amount < sender.getBalance():
            sender.setBalance(-amount)
            receiver.setBalance(amount)
            # self.balance = self.balance + self.amount
            print("Account balance sender has been updated : $", sender.getBalance())
            print("Account balance receiver has been updated : $", receiver.getBalance())
            self.recTransaction(sender, receiver, "Successful", amount, label=description)

        else:
            self.recTransaction(sender, receiver, "Unsuccessful", amount, label=description)

    def withdrawal(self, amount, withdrawer, description=None):
        if 0 < amount < withdrawer.getBalance():
            withdrawer.setBalance(-amount)
            self.recTransaction(withdrawer, withdrawer, "Successful", amount, label=description)

        else:
            self.recTransaction(withdrawer, withdrawer, "Unsuccessful", amount, label=description)

    def getTransaction(self):
        return self.transaction

    def recTransaction(self, sender, receiver, status, amount, datetime=None, label=None):
        # sender.__dict__.update(receiver.__dict__)

        self.data["sender_name"] = sender.__dict__["name"]
        self.data["sender_age"] = sender.__dict__["age"]
        self.data["sender_gender"] = sender.__dict__["gender"]
        self.data["sender_iban"] = sender.__dict__["iban"]
        self.data["sender_balance"] = sender.__dict__["balance"]

        self.data["receiver_name"] = receiver.__dict__["name"]
        self.data["receiver_age"] = receiver.__dict__["age"]
        self.data["receiver_gender"] = receiver.__dict__["gender"]
        self.data["receiver_iban"] = receiver.__dict__["iban"]
        self.data["receiver_balance"] = receiver.__dict__["balance"]

        self.data["status"] = status
        self.data["amount"] = amount
        self.data["transaction"] = self.getTransactioncode("".join([str(x) for x in self.data.values()]).encode("utf8"))
        self.data["label"] = label
        self.getTransactioncode("".join([str(x) for x in self.data.values()]).encode("utf8"))
        print(str("".join([str(x) for x in self.data.values()]).encode(
            "utf8")))
        with open('file.json', 'a') as outfile:
            outfile.write(json.dumps(self.data))
            outfile.write(",\n")
            outfile.close()

        print(self.data)
        self.transaction.append(json.dumps(self.data))

    # def save(self):
    #   with open("record.")
