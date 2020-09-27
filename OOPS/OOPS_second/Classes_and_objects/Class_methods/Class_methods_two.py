# %%

from employee import Employee
from datetime import datetime

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f'{self.name} & {self.age}')

    @classmethod
    def from_str(cls, data_string):
        name, age = data_string.split(',')
        return cls(name, int(age)) # __init__ method called because we are creating a class instance object

    @classmethod
    def from_dict(cls, data_dict):
        return cls(data_dict['name'], data_dict['age'])

    @classmethod
    def from_employee(cls, object_emp):
        name = object_emp.first_name+' '+object_emp.last_name
        age = datetime.today().year - object_emp.birth_year
        return cls(name, age)

p1 = Person('a', 10)
p2 = Person('b', 20)

# Factory methods
    # We want to create a Person instance object from different kinds of data from some file
    # Python doesnt support function overloading, so only one __init__ method
    # create class methods
str_data = 'Jim, 20'
p3 = Person.from_str(str_data)
p3.display()
dict_data = {'name':'John', 'age':30}
p4 = Person.from_dict(dict_data)
p4.display()

emp_inst_obj = Employee('Maria', 'DB', 1900, 20000)
p5  = Person.from_employee(emp_inst_obj)
p5.display()

# %%
