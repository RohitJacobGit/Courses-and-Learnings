class Employee:
    def __init__(self, first_name, last_name, birth_year, salary): 
        self.first_name = first_name  
        self.last_name = last_name  
        self.birth_year = birth_year
        self.salary = salary
        
    def show(self): 
        print(f'I am {self.first_name} {self.last_name} born in {self.birth_year}')
