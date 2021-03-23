class User:

    def __init__(self, name, age, gender, iban):
        self.name = name
        self.age = age
        self.gender = gender
        self.iban = iban

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name", self.name)
        print("Age", self.age)
        print("Gender", self.gender)