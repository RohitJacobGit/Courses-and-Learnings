# No concept of public/private in Python
# _abc can be used to suggest as private
    # for internal use of the class and should not be accessed outside it
# __abc: attribute will not be directly visible from outside the class: name mangling
    # _ClassName__abc
    # Purpose: No name clash with subclasses
# To avoid clash in keyword name & variable name : class_ , range_

# %%
class Product:

    def __init__(self):
        self.data = 10
        self._data = 10
        self.__somevalue = 20

    def methodA(self):
        pass

    def _methodB(self):
        pass

    def __methodC(self):
        pass

p = Product()
print(p.data)
print(p._data)
#print(dir(p))
print(p._Product__somevalue)

# %%
