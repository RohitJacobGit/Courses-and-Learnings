class MyClass:

    a = 5

    def method1(self):
        print(self.a)

    # class method: associated wiht the class itself not with instance object
    # using cls as a convention just like self: some other word can also be used
    # can be invoked using a class name or an instance
    # cant access instance variables as it doesnt have self parameter
    # generally created to access class variables 
    # class methods used to define factory methods
    @classmethod
    def method2(cls):
        print(cls.a)

# classmethod can be called without creating an instance object of the class
MyClass.method2()