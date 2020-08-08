class Account:

    rate = 5


a1 = Account()
a2 = Account()

print(Account.rate, id(Account.rate))
print(a1.rate, id(Account.rate))
print(a2.rate, id(Account.rate))

Account.rate = 6
print(Account.rate, id(Account.rate))
print(a1.rate, id(Account.rate))
print(a2.rate, id(Account.rate))

a1.rate = 7
print(Account.rate, id(Account.rate))
print(a1.rate, id(a1.rate))  # Only the value associated with this instance changes
print(a2.rate, id(a2.rate))
