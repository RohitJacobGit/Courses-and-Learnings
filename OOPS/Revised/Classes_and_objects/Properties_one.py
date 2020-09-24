# %%
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # set_age constraint checked here as well since age is now being treated as an instance variable

    def display(self):
        print('Name and age: ', self.name, self.age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if 20 < new_age < 30:
            self._age = new_age
        else:
            raise ValueError('Age must be between 20 and 30')


if __name__=='__main__':
    p = Person('Anand', 25)
    p.display()
    p.age = 23
    print(p.age)
    
# %%
