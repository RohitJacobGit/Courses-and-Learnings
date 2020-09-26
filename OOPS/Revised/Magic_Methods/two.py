class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr = self.nr * -1
            self.dr = self.dr * -1
        self._reduce()

    # @string in Java
    # readable representation of the object
    def __str__(self):
        return f'{self.nr}/{self.dr}'

    def _reduce(self):
        h = Fraction.hcf(self.nr, self.dr)
        if h == 0:
            return

        self.nr = self.nr/h
        self.dr = self.dr/h

    @staticmethod
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x % s == 0 and y % s == 0:
                break
            s -= 1
        return s

    def __mul__(self, new_frac):
        if isinstance(new_frac, int):
            new_frac = Fraction(new_frac)
        mult_nr = self.nr * new_frac.nr
        mult_dr = self.dr * new_frac.dr
        f = Fraction(mult_nr, mult_dr)
        f._reduce()
        return f

    def __add__(self, new_frac):
        if isinstance(new_frac, int):
            new_frac = Fraction(new_frac)
        added_nr = self.nr*new_frac.dr + self.dr*new_frac.nr
        added_dr = self.dr*new_frac.dr
        f = Fraction(added_nr, added_dr)
        f._reduce()
        return f

    # commutative law
    def __radd__(self, new_frac):
        return self.__add__(new_frac)

    def __sub__(self, new_frac):
        if isinstance(new_frac, int):
            new_frac = Fraction(new_frac)
        added_nr = self.nr*new_frac.dr - self.dr*new_frac.nr
        added_dr = self.dr*new_frac.dr
        f = Fraction(added_nr, added_dr)
        f._reduce()
        return f

    # @equals in Java
    def __eq__(self, new_frac):
        return (self.nr*new_frac.dr) == (self.dr*new_frac.nr)


f1 = Fraction(2, 3)
#f1.show()
f2 = Fraction(3, 4)
#f2.show()

print(f1+3)
print(3+f1) #error before __radd__
