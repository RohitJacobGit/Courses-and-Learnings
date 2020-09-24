# %%
class Account:

    rate = 5


a1 = Account()
a2 = Account()

# all print 5
print(Account.rate)
print(a1.rate)
print(a2.rate)

Account.rate = 6
# all print 6
print(Account.rate)
print(a1.rate)
print(a2.rate)

a1.rate = 7
print(Account.rate) # prints 6
print(a1.rate)  # prints 7
print(a2.rate)  # prints 6

# working on class variable? - access via Classname.variable
# working on instance variable? - access via self.variable
