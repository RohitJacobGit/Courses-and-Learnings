# %%
class Product:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def value(self):
        return self._x

    @value.setter
    def value(self, val):
        self._x = val

    @value.deleter
    def value(self):
        print('value deleted')

p = Product(12, 14)

# %%
