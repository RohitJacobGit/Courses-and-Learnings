class Person:
    # def set_details(self, name, age):
    #     '''
    #     self.name and self.age are instance variables
    #     instance variables can be used anywhere in the class but function parameters cannot be
    #     name and age are function parameters
    #     '''
    #     self.name = name
    #     self.age = age

    #     self.name and self.age are instance variables
    #     and name and age are local variables

    #     self = 'this' in java

    # __init__ is dunkel method
    # only one __init__ can be present in a class
    # python doesnt support function overloading
    # executed as soon as the class instance has been related
    # any code which should be executed just after the object creation
    # Doesnt need to be called explicitly
    # Just like a constructor in java
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('Hello !!', self.name, self.age)
        self.greet()

    def greet(self):
        if self.age < 30:
            print('Cool, you are below 30 and you are allowed', self.age)
        else:
            print('Oh no, you are not welcomed!!')

    def noninstance_Var(self):
        var_1 = 'abc'
        print(var_1)


p1 = Person('Rohit', 23)
# p1.set_details('ROhit', 30) can be removed after we define __init__ method
p1.display()


p2 = Person('Anand', 40)
# p2.set_details('Anand', 30) throws error if not called
p2.display()

# p1.noninstance_Var()
# p2.noninstance_Var()
