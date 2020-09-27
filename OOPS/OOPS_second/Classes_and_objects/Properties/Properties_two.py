# %%
class Employee:

    def __init__(self, name, password, salary):
        self._name = name
        self._password = password
        self._salary = salary

    # getter : read-only
    @property
    def name(self):
        return self._name

    # not readable, write-only
    @property
    def password(self):
        return AttributeError('Not Readable')

    # not readable, write-only
    @password.setter
    def password(self, new_password):
        self._password = new_password

    # read and write
    @property
    def salary(self):
        return self._salary

    # read and write
    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary

e = Employee('Anand', 'abc@123', 20000)

# %%
