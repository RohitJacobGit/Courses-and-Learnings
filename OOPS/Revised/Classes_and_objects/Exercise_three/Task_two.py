class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr = self.nr * -1
            self.dr = self.dr * -1
        self._reduce()

    def show(self):
        print(f'{self.nr} / {self.dr}')

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

    def multiply(self, new_frac):
        if isinstance(new_frac, int):
            new_frac = Fraction(new_frac)
        mult_nr = self.nr * new_frac.nr
        mult_dr = self.dr * new_frac.dr
        f = Fraction(mult_nr, mult_dr)
        f._reduce()
        return f

    def add(self, new_frac):
        if isinstance(new_frac, int):
            new_frac = Fraction(new_frac)
        added_nr = self.nr*new_frac.dr + self.dr*new_frac.nr
        added_dr = self.dr*new_frac.dr
        f = Fraction(added_nr, added_dr)
        f._reduce()
        return f


f1 = Fraction(6, 36)
f1.show()
f2 = Fraction(2, -12)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5)
f3.show()
f3 = f1.multiply(5)
f3.show()
