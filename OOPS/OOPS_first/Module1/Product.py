class Product:

    def __init__(self):
        self.data1 = 10
        # Private variable
        self._data2 = 20
        self.__data3 = 30

    def methodA(self):
        pass

    # Although a private method, it can be called by anyone
    # It is used a trust that this shoˆuld not be mingled with
    # It can be called outside the class
    def _methodB(self):
        print('I am a private method although it can be called outside the class')

    def __methodC(self):
        print('class name appended to this method')   


p = Product()
print(p._data2)  # dont access private members outside class

# Private method
p._methodB()  # dont access private members outside class

# Error: print(p.__data3)
# Error: print(p.__methodC)
print(dir(p))
print(p._Product__data3)  # class name has been appended
print(p._Product__methodC())
