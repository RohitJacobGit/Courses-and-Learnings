class Product_1:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def display(self):
        print(self._x, self._y)

    # use this method as an class instance variable
    # we dont require to specify paranthesis: p.value_x
    # getter
    @property
    def value_x(self):
        return self._x

    # setter
    @value_x.setter
    def value_x(self, val):
        self._x = val

    # @property
    # def value_y(self):
    #     return self._y
    #
    # @value_y.setter
    # def value_y(self, val):
    #     self._y = val


p = Product_1(10, 66)
p.display()
print(p.value_x)
# print(p.value_x+5)

# We cannot assign a new value, Error: p.value = 10
# This can be done by adding a new method with @value_x.setter
p.value_x = 45
print(p.value_x)

# print(p.value_y)
