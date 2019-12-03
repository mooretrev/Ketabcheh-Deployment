class Book:
    title = ''
    description = ''
    prices = []
    rating = ''
    vendors = []
    authors = []
    publisher = ''
    year = ''

    def __init__(self, title, desc, prices, rating, authors, publisher, year, isbn):
        self.title = title
        self.description = desc
        self.rating = rating
        self.prices = prices # prices from low to high
        self.vendors = [] # link to external website where the user can buy the book
        self.authors = authors
        self.publisher = publisher
        self.year = year
        self.isbn = isbn
        self.released = True

    def display(self):
        print("Title: " + self.title)
        print('Description: ' + self.description)
        print('Raing: ' + self.rating)
        print('Prices: \n\tUsed: ' +
              str(self.prices[0]) + "\n\tNew: " + str(self.prices[1]))
        print('Authors: ' + str(self.authors))
        print('Publisher: ' + self.publisher)
        print('Year: ' + self.year)
        print('ISBN: ' + self.isbn)

