class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        # self.diagonal = ((self.length)**2 + (self.breadth)**2)**0.5
        # diagonal wont change if we change lenght or breadth
        # for the diagonal to change, define it as a getter method

    # add new method
    # use @property if we want to access it without paranthesis in line24
    def diagonal(self):
        return ((self.length)**2 + (self.breadth)**2)**0.5

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)


rect = Rectangle(10, 20)
print(rect.area())
print(rect.perimeter())
# print(rect.diagonal)
print(rect.diagonal())

# changing the length
rect.length = 20
print(rect.area())  # changes
print(rect.perimeter())  # changes
# print(rect.diagonal)  # doesnt change, why? - because it is calculated only once during object instantiation
print(rect.diagonal())  # now changed
