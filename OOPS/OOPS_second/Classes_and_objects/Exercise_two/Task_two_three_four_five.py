# %%
class Book:

    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price # constraint check valid using setter method
        self.copies = copies

    def in_stock(self):
        if self.copies>0:
            return True
        else:
            return False

    def sell(self):
        if self.in_stock()==True:
            self.copies = self.copies - 1
        else:
            print('out of stock')

    @property
    def price(self):
          return self._price

    @price.setter
    def price(self, new_price):
        if 50 <= new_price <= 1000:
              self._price = new_price
        else:
              raise ValueError ('Price cannot be less than 50 or more than 1000')

    def display(self):
        print(self.title)
        print(f'ISBN : {self.isbn}')
        print(f'Price : {self.price}')
        print(f'Number of copies : {self.copies}')
        print('.' * 50)


# if __name__=='__main__':
#     book1 = Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 200, 10)
#     book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
#     book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
#     book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

#     book1.display()
#     book2.display()
#     book3.display()
#     book4.display()

list_of_instances = []
book1 = Book('957-4-36-547417-1', 'Learn Physics', 'Stephen', 'CBC', 350, 200, 10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 10,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

list_of_instances.append(book1)
list_of_instances.append(book2)
list_of_instances.append(book3)
list_of_instances.append(book4)

for books in list_of_instances:
    books.display()

jack_books = [
    book.title for book in list_of_instances if book.author == 'Jack']

# %%
