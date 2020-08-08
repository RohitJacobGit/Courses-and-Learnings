from Employee_1 import Employee_1
from datetime import datetime


# Point: static methods neither belong to instance nor to a class
# They are used as a helper method and can be called without the help of a class or an instance
class Person_3:

    # class variables
    species = 'Human'
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person_3.count = Person_3.count + 1

    def display(self):
        print(f'{self.name} and {self.age}')

    # class method
    # for accessing class variables
    # it cannot work with instance variables as it doesnt have self keyword
    # can be called using a class instance but makes more sense to call with a class name
    # can use some other name instead of 'cls' but not 'self'
    @classmethod
    def show_count(cls):
        print(f'{cls.count} instances of {cls.species}')

    # class methods can be used as Factory methods
    @classmethod
    def from_str(cls, s):
        name, age = s.split(',')
        return cls(name, int(age))  # class instance: init method called

    # class methods can be used as Factory methods
    @classmethod
    def from_dict(cls, d):
        return cls(d['name'], d['age'])  # class instance: init method called

    @classmethod
    def from_employee(cls, emp):
        name = emp.first_name+' '+emp.last_name
        age = datetime.today().year - emp.birth_year
        return cls(name, age) # class instance: init method called


# Calling class method with class name
Person_3.show_count()

p1 = Person_3('cbz', 30)
p2 = Person_3('mcf', 40)
p3 = Person_3('ekw', 50)
p4 = Person_3('qkl', 60)

# p1.display()
# p2.display()
# p3.display()
# p4.display()

# Calling class method with class name
Person_3.show_count()

# Calling class method with instance works but doesnt make sense
p1.show_count()

# factory methods: for creating a person instance for different type of inputs
# calling factory methods
# create person instance from string type
fm_instance_1 = Person_3.from_str('ROhit, 12344')
fm_instance_1.display()

# create person instance from dictionary type
fm_instance_2 = Person_3.from_dict({'name': 'anand', 'age': 32})
fm_instance_2.display()

# create person instance from employee type
emp = Employee_1('Rohit', 'Anand', 1994, 2000)
fm_instance_3 = Person_3.from_employee(emp)
fm_instance_3.display()
