class Product:
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self._discount = discount

    @property
    def selling_price(self):
        return (self.marked_price - ((self.marked_price*self._discount)/100))

    @property
    def discount(self):
        if self.selling_price>500:
            return self._discount+2
        else:
            return self._discount

    @discount.setter
    def discount(self, new_discount):
        self._discount = new_discount

    def display(self):
        print(self.id,  self.marked_price,  self.discount)


p1 = Product('X879', 400, 6)
p2 = Product('A234', 100, 5)
p3 = Product('B987', 990, 4)
p4 = Product('H456', 800, 6)

print('SP for', p1.id, ' is ',p1.selling_price)
print(p2.id, p2.selling_price)
print(p3.id, p3.selling_price)
print(p4.id, p4.selling_price)

p4.discount = 10
print(p4.id, p4.selling_price)
