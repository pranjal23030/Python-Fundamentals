class Book:
    """fields: title, author, year, price"""

    # constructor with arguments

    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    # returns details of Book object as a string
    def __str__(self):
        return "{0} ({1} by {2} costs {3:1.2f})".format(self.title, self.author, self.year, self.price)

    # setter methods
    def set_title(self, new_title):
        self.title = new_title

    def set_author(self, new_author):
        self.author = new_author

    def set_year(self, new_year):
        self.year = new_year

    def set_price(self, new_price):
        self.price = new_price

    # getter methods

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price

    # test for equality, only 3 attributes are used here : title, author, year

    def __eq__(self, other):
        return self.get_title().upper() == other.get_title().upper() and self.get_author().upper() == other.get_author().upper() and \
            self.get_year() == other.get_year()

    # these methods are for sorting
    def __lt__(self, other):
        return self.get_price() < other.get_price()

    def __le__(self, other):
        return self.get_price() <= other.get_price()


b1 = Book("Harry Potter and the prisoner of Azkaban", "JK Rowling", 2012, 200.0)
b2 = Book("Harry Potter and the prisoner of Azkaban", "JK Rowling", 2012, 200.0)

print(b1 == b2)
print(id(b1))
print(id(b2))
print()

print(b1 < b2)
print(b1 <= b2)
print()

blast = [Book('Basic Java', 'James', 2010, 20.45),
         Book('Python Programming', 'Jenny', 2009, 20.00),
         Book('C++', 'James', 2011, 15.0)]

for p in sorted(blast):
    print(p)
print()
