class Person_3:

    # class variables, dont belong to any instances
    species = 'Human'
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person_3.count = Person_3.count + 1
        self.display()

    def display(self):
        print(f'{self.name} and {self.age} and instance count {Person_3.count}')


p1 = Person_3('cbz', 30)
p2 = Person_3('mcf', 40)
p3 = Person_3('ekw', 50)
p4 = Person_3('qkl', 60)

# p1.display()
# p2.display()
# p3.display()
# p4.display()

print(Person_3.species)

# NUmber of instances
print(Person_3.count)
