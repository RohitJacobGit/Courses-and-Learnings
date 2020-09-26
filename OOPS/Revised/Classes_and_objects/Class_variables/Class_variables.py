# %%
class Person:

    # Class variables - Belongs to the class and not to class instance objects
    # Shared by all the instances of the class
    # species will be same for all instance objects
    # if same name as instance var then the instance var hides the class var
    # can be accessed even before an instance object is created
    species = 'Homo Sapiens'

    # class variable to count the number of instances created
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count = Person.count + 1

    def display(self):
        print(f'{self.name} & {self.age} & {self.species} or {Person.species}')


p1 = Person('a',10)
p2 = Person('b',20)

print(Person.species)
print(p1.species)
print(p2.species)
# print(Person.name) # error
print(id(Person.species) == id(p1.species) == id(p2.species))

print('# instance objects created: ', Person.count)
# %%
