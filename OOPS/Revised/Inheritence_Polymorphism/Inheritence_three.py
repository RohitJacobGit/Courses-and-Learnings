class Person:
    def __init__(self, name, age, address, phone):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone

    def greet(self):
        print('Hello I am', self.name)

    def is_adult(self):
        if self.age > 18:
            return True
        else:
            return False

    def contact_details(self):
        print(self.address, self.phone)


class Employee(Person):
    def __init__(self, name, age, address, phone, salary, office_address, office_phone):
        # calling base class method also
        # using super() avoids adding self in argument and is preferred
        super().__init__(name, age, address, phone)
        self.salary = salary
        self.office_address = office_address
        self.office_phone = office_phone

    def calculate_tax(self):
        if self.salary < 5000:
            return 0
        else:
            return self.salary * 0.05

    # Overriding
    def contact_details(self):
        super().contact_details()  # calling base class method also
        print(self.office_address, self.office_phone)


e = Employee('abcde', 23, 'India', 12343, 8000, 'ABC Street', '384923993')
p = Person('blah', 3, 'Peru', 99999)
# e.greet()
# e.contact_details()
# print(isinstance(e, Employee))
# print(isinstance(e, Person))
# print(issubclass(Employee, Person))
# print(issubclass(Person, object))
# print(issubclass(str, object))
# print(issubclass(int, object))

print(e.calculate_tax())
e.contact_details()
p.contact_details()
