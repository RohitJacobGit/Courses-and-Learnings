class Person_2:

    def __init__(self, name, age):
        self.name = name
        self.age = age  # self.age is not a variable, instead its a method

    def display(self):
        print(self.name, self._age)

    # getter method
    @property
    def age(self):
        # access private member using getter method
        return self._age

    # setter method
    @age.setter
    def age(self, new_age):
        if 20 < new_age < 30:
            self._age = new_age
        else:
            raise ValueError('Age should be between 20 and 30')


if __name__ == '__main__':
    p2 = Person_2('Rohit', 23)
    p2.display()
    print(p2.age)
    p2.age = 23
    print(p2.age)
    # Error: p2.age = 100
    p2.age = p2.age + 1
    print(p2.age)
