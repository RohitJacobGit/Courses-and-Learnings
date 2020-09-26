class Employee:

    domains = set()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        # self._get_domains()
        Employee.domains.add(self.email.split('@')[1].split('.')[0])

    def display(self):
        print(self.name, self.email)
    
    # def _get_domains(self):
        # domain = email[email.index('@')+1:]
        # Employee.domains.add(domain)

        # Employee.domains.add(self.email.split('@')[1].split('.')[0])

e1 = Employee('John','john@gmail.com')
e2 = Employee('Jack','jack@yahoo.com')
e3 = Employee('Jill','jill@outlook.com')
e4 = Employee('Ted','ted@yahoo.com')
e5 = Employee('Tim','tim@gmail.com')
e6 = Employee('Mike','mike@yahoo.com')

print(Employee.domains)
