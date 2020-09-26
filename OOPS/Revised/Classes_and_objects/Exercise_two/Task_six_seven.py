class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr = self.nr * -1
            self.dr = self.dr * -1

    def show(self):
        print(f'{self.nr} / {self.dr}')

    def multiply(self, new_frac):
        if isinstance(new_frac, int):
            new_frac = Fraction(new_frac)
        mult_nr = self.nr * new_frac.nr
        mult_dr = self.dr * new_frac.dr
        return Fraction(mult_nr, mult_dr)

    def add(self, new_frac):
        if isinstance(new_frac, int):
            new_frac = Fraction(new_frac)
        added_nr = self.nr*new_frac.dr + self.dr*new_frac.nr 
        added_dr = self.dr*new_frac.dr 
        return Fraction(added_nr, added_dr)

f1 = Fraction(2, 3)
f1.show()
f2 = Fraction(3, 4)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.multiply(5)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5)
f3.show()
