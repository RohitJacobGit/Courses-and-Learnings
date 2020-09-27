class Person:

    # dunder or magic methods: called implicitly
    # __init__ = looks like a constructor but not a constructor
            # class object/instance is already created before __init__ is called
            # called immediately after instance is created
            # first method to be called on newly created instance object(self)
            # doesnt contruct the instance object
            # initialized the already constructed instance object
            # only 1 __init__ method is a class
            # Python: no function overloading
    # Actual constructor: __new__
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_name(self):
        print('name is: ', self.name)

    def display_age(self):
        print('age is: ', self.age)

    
p1 = Person('tom',50)
p1.display_name()
p1.display_age()

p1 = Person('harry', 30)
p1.display_name()
p1.display_age()
