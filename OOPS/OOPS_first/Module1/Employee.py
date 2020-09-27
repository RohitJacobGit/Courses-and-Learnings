class Employee:

    def __init__(self, name, password, salary):
        self._name = name
        self._password = password
        self._salary = salary

    # only read
    @property
    def name(self):
        return self._name

    # only write
    @property
    def password(self):
        raise AttributeError('password not readable')

    # only write
    @password.setter
    def password(self, new_password):
        self._password = new_password

    # read
    @property
    def salary(self):
        return self._salary

    # write
    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary


e = Employee('Rohit', 'abc@123', 25000)
# Error: password is write only : print(e.password)
# Error: name read only : e.name = 'Anand'

print(e.name)  # name is read only
print(e.salary)
e.password = '123@abc'
e.salary = 50000
