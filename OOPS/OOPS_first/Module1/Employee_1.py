class Employee_1:

    def __init__(self, first_name, last_name, birth_year, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.salary = salary

    def show(self):
        print(f'First name: {self.first_name}, Last name: {self.last_name} \
              , Birth year: {self.birth_year}, Salary: {self.salary}')
