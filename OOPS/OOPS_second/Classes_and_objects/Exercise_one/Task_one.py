class Bank:
    def set_details(self, name, balance=0):
        self.name = name
        self.balance = balance

    def display(self):
        print('name & balance: {0}, {1} '.format(self.name, self.balance))

    def withdraw(self, amount):
        self.amount = amount
        self.balance = self.balance - self.amount

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount


b1 = Bank()
b1.set_details('Arzoo', 20000)
b1.display()

# b1.withdraw(2000)
# b1.display()
# b1.deposit(3000)
# b1.display()
