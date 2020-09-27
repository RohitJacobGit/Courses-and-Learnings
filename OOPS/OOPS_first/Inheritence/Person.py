class Person:
    def __init__(self, name, age, address, phone):
        self.name = name
        self._age = age
        self._address = address
        self._phone = phone

    def greet(self):
        print('Hi, ', self.name)

    def is_Adult(self):
        if self._age > 30:
            return True
        else:
            return False

    @property
    # access as a variable
    def get_age(self):
        return self._age

    @property
    # access as a variable
    def get_address(self):
        return self._address

    def get_contact_details(self):
        print(self._address, ' ', self._phone)


class Employee(Person):
    def __init__(self, name, age, address, phone, salary, office):
        # self.name = name
        # self._age = age
        # self._address = address
        # self._phone = phone

        # Person.__init__(self, name, age, address, phone)

        super().__init__(name, age, address, phone)
        self.salary = salary
        self.office = office

    def calculate_tax(self):
        if self.salary < 5000:
            return 0
        else:
            return self.salary * 0.1

    # override baseclass method
    def get_contact_details(self):
        # print(self._address, ' ', self._phone)
        # Person.get_contact_details(self)
        
        super().get_contact_details()
        print(self.salary, ' ', self.office)


emp = Employee('rohit', '21', 'Bremen', '0000000', 7000, 'Bangalore')

# print(emp.get_age)
# print(emp.name)
print(emp.get_contact_details())

# print(isinstance(emp, Employee))
# print(isinstance(emp, Person))
#
# print(issubclass(Person, object))
# print(issubclass(Employee, Person))
# print(issubclass(int, object))

print('tax : ', emp.calculate_tax())
