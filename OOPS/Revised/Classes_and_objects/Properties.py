# %%
class Product:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def display(self):
        print(self._x, self._y)

    # treated as a variable now, getter method
    # p.value() is now p.value
    # p.value = 15 assignment wont work if setter not defined
    @property 
    def value(self):
        return self._x

    # p.value = 15
    # getter and setter name should be same
    @value.setter
    def value(self, val):
        self._x = val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self._y = val


p = Product(12, 14)
# p.value will output 12
# p.value = 15
# p.value will output 15

# p.y will output 12
# p.y = 15
# p.y will output 15

# %%
