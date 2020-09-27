class Employee:

    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self._check_domain()
        
    def _check_domain(self):
        for domain in Employee.allowed_domains:
            if self.email.split('@')[1] != domain:
                print(domain)
                raise RuntimeError('Not allowed')

    def display(self):
        print(self.name, self.email)

e1 = Employee('John', 'john@gmail.com')
e2 = Employee('Jack', 'jack@yahoo.com')
e3 = Employee('Jill', 'jill@outlook.com')
e4 = Employee('Ted', 'ted@yahoo.com')
e5 = Employee('Tim', 'tim@xmail.com')
