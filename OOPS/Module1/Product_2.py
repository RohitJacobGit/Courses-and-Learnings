class Product_2():
    def __init__(self, id, marked_price, discount):
        self.id = id
        self.marked_price = marked_price
        self._discount = discount

    @property
    def selling_price(self):
        return self.marked_price*(1 - self.discount*0.01) #discount method

    @property
    def discount(self):
        if self.marked_price > 500:
            return self._discount+2
        else:
            return self._discount

    @discount.setter
    def discount(self, new_discount):
        self._discount = new_discount #discount variable

    def display(self):
        print(self.id,  self.marked_price,  self.discount)


p1 = Product_2('X879', 400, 6)
p2 = Product_2('A234', 100, 5)
p3 = Product_2('B987', 990, 4)
p4 = Product_2('H456', 800, 6)

print(p1.id, p1.selling_price)
print(p2.id, p2.selling_price)
print(p3.id, p3.selling_price)
print(p4.id, p4.selling_price)

p4.discount = 10
print(p4.id, p4.selling_price)
