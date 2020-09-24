# %%
class Person:

    species = 'Homo Sapiens'
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count = Person.count + 1

    def display(self):
        print(f'{self.name} & {self.age} & {self.species} or {Person.species}')

    @classmethod
    def show_count(cls):
        print(f'{cls.count} & {cls.species}')

Person.show_count()
p1 = Person('a', 10)
p2 = Person('b', 20)
Person.show_count()


# %%
