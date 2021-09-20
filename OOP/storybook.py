class StoryBook:

    # Class Variable
    no_of_books = 0

    discount = 0.5

    def __init__(self, name, price, author_name, author_born, no_of_pages):
        # setting the instance variables here
        print("Hello")
        self.name = name
        self.price = price
        self.author_name = author_name
        self.author_born = author_born
        self.publishing_year = 2021
        self.no_of_pages = no_of_pages
        StoryBook.no_of_books +=1

    # regular method
    def get_book_info(self):
        print(f'The book name: {self.name}, price: {self.price}, pages: {self.no_of_pages}')

    def get_author_info(self):
        print(f'The Author name is: {self.author_name}, born: {self.author_born}')

    # applying discount to an instance
    def apply_discount(self):
        self.price = int(self.price - self.price * self.discount)

    # Method to change price
    def set_price(self, new_price):
        self.price = new_price

    # Class Method 1
    @classmethod
    def set_discount(cls, new_discount):
        cls.discount = new_discount

    # Class Method 2
    @classmethod
    def construct_from_string(cls, book_str):
        name, price, author_name, author_born, pages = book_str.split(',')

        return cls(name, price, author_name, author_born, pages)

    # Static Methods
    @staticmethod
    def is_new(publishing_year):
        if publishing_year > 2016:
            print('Yes it is a new book!')
        else:
            print('No it is not!')


# creating an instance/ object of the StoryBook Class
book_1 = StoryBook('Hamlet', 350, 'Shakespeare', 1564, 500)
book_2 = StoryBook('the_kite_runner', 200, 'Ashok',1997, 300)

book_2.get_book_info()
book_2.get_author_info()

StoryBook.get_author_info(book_1)

# print(book_1.no_of_books)
# print(book_2.no_of_books)
# print(StoryBook.no_of_books)
# print(book_2.price)
# book_2.discount = 0.3
# book_2.apply_discount()
# print(book_2.price)

# print(book_1.price)
# print(book_1.discount)
# StoryBook.set_discount(0.6)
# print(book_1.apply_discount())
# print(book_1.price)

book_str = 'Harry Potter, 200, JK Rowling, 1970, 400'
harry_potter = StoryBook.construct_from_string(book_str)
print(harry_potter.name)

StoryBook.is_new(book_1.publishing_year)
