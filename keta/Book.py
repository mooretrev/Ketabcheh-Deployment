class Book:
    title = ''
    description = ''
    prices = []
    rating = ''
    vendors = []
    authors = []
    publisher = ''
    year = ''

    def __init__(self, title, desc, prices, rating, authors, publisher, year, isbn, released, vendors, numPrices):
        self.title = title
        self.description = desc
        self.rating = rating
        self.prices = prices  # prices from low to high
        self.vendors = vendors  # link to external website where the user can buy the book
        self.authors = authors
        self.publisher = publisher
        self.year = year
        self.isbn = isbn
        self.released = released
        self.arrayLen = numPrices

    def display(self):
        print("Title: " + self.title)
        print('Description: ' + self.description)
        print('Raing: ' + self.rating)
        print('Prices: ', end='')
        print(self.prices)
        print('Vendors: ', end='')
        print(self.vendors)
        print('Authors: ' + str(self.authors))
        print('Publisher: ' + self.publisher)
        print('Year: ' + self.year)
        print('ISBN: ' + self.isbn)
        print('Released: ' + str(self.released))
        print('Array Len ' + str(self.arrayLen))
