class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius < 0:
            print('Radius should be positive')
        else:
            self._radius = new_radius

    @property
    def diameter(self):
        return 2*self._radius

    @property
    def circumference(self):
        return 2 * 3.14 * self._radius

    def area(self):
        return 3.14*self._radius*self._radius


c1 = Circle(7)
print(c1.radius, c1.diameter, c1.circumference, c1.area())
