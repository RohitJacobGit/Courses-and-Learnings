class MyClass:

    a = 5

    def method1(self):
        print(self.a)

    @classmethod
    def method2(cls):
        print(cls.a)

    # No class object or instance object
    # cant access class state nor instance state
    # helper or utility method some logic related to class: static method
    @staticmethod
    def method3(m, n):
        return m+n

MyClass.method2()
