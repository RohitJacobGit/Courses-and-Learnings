# we want the age to be between 20 and 30
# set age as a private variable : _age
# private method : def _something()
# dont access provate memebers outside the class
# to differentiate between inbuilt names use 'somename_' with a trailing _
# access private members after defining a getter method using @property
class Person_1:

    def __init__(self, name, age):
        self.name = name
        # self._age = age
        if 20 < age < 30:
            self._age = age
        else:
            raise ValueError('Age should be between 20 and 30')

    def display(self):
        print(self.name, self._age)

    def set_age(self, new_age):
        if 20 < new_age < 30:
            self._age = new_age
        else:
            raise ValueError('Age should be between 20 and 30')

    def get_age(self):
        return self._age


if __name__ == '__main__':
    # p = Person_1('Rohit', 30)
    # p.display()
    # # Error: p.set_age(100)
    # p.set_age(23)
    # p.display()
    # # Increase the age by 1
    # p.set_age(p.get_age()+1)
    # p.display()

    # This restriction was not there during object instantiation
    # So we add this restriction in the __init__ method
    p1 = Person_1('Anand', 21)
    p1.display()
