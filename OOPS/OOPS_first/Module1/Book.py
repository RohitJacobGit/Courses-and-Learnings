class Book:

    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self._price = price
        self.copies = copies

    def in_stock(self):
        if self.copies > 0:
            return True
        else:
            return False

    def sell(self):
        if self.in_stock():
            self.copies = self.copies - 1
        else:
            print('Book is out of stock')

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if 50 <= new_price <= 1000:
            self._price = new_price
        else:
            raise ValueError('Price cannot be less than 10 or more than 500')

    def display(self):
        print(self.isbn, ' ', self.title, ' ', self.price, ' ', self.copies)


book1 = Book('957-4-36-547417-1', 'Learn Physics',
             'Stephen', 'CBC', 350, 200, 10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry',
             'Jack', 'CBC', 400, 220, 20)
book3 = Book('957-7-39-347216-2', 'Learn Maths', 'John', 'XYZ', 500, 300, 5)
book4 = Book('957-7-39-347216-2', 'Learn Biology', 'Jack', 'XYZ', 400, 200, 6)

book_list = [book1, book2, book3, book4]

for book in book_list:
    book.display()

jack_list = [book.title for book in book_list if book.author == 'Jack']
print(jack_list)
