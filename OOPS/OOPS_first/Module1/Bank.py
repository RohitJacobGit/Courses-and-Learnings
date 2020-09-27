class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print(self.name, ' ', self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount


b1 = Bank()
# b1.set_details('Rohit') # Default = 0
b1.set_details('Rohit', 10000)  # Default = 0
b1.display()
b1.withdraw(5000)
b1.display()
b1.deposit(10000)
b1.display()
