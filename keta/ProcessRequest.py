import requests
import json
# from .Book import Book
from Book import Book

'''
    Book Run API Reference: https://booksrun.com/page/api-reference
'''
# OLIN


class ErrorNoReviewFound(BaseException):
    pass


def process_isbn(isbn, generalInfo=None):
    if generalInfo is None:
        generalInfo = google_books_search_by_isbn(
            isbn)['items'][0]
    priceInfo = book_run_api_call(isbn)['result']['offers']['booksrun']
    try:
        ratingInfo = good_book_review(isbn)['books'][0]
    except ErrorNoReviewFound:
        ratingInfo = {'average_rating': 'No reviews yet!'}

    title = generalInfo['volumeInfo']['title']
    description = generalInfo['volumeInfo']['description']
    authors = generalInfo['volumeInfo']['authors']
    publisher = generalInfo['volumeInfo']['publisher']
    date = generalInfo['volumeInfo']['publishedDate']
    availableGoogle = generalInfo['saleInfo']['saleability'] == "FOR_SALE"

    # [bookrun used, bookrun new, google listprice]

    pricesVendors = [{'price': -1 if priceInfo['used'] ==
                      'none' else priceInfo['used']['price'], 'url': -1 if priceInfo['used'] ==
                      'none' else priceInfo['used']['cart_url'], 'type':'bookrun used'},
                     {'price': -1 if priceInfo['new'] ==
                      'none' else priceInfo['new']['price'], 'url': -1 if priceInfo['new'] ==
                      'none' else priceInfo['new']['cart_url'], 'type':'bookrun new'},
                     {'price': generalInfo['retailPrice']['amount'] if availableGoogle else -1,
                      'url': generalInfo['buyLink'] if availableGoogle else -1,
                      'type': 'google'}]

    rating = ratingInfo['average_rating']
    pricesVendors = sorted(pricesVendors, key=lambda i: i['price'])

    prices = []
    for p in pricesVendors:
        if p['price'] != -1:
            prices.append(p['price'])

    vendors = []
    for v in pricesVendors:
        if v['url'] != -1:
            vendors.append(v['url'])
    print(vendors)

    purchasable = False
    for p in pricesVendors:
        if p['price'] != -1:
            purchasable = True

    print(pricesVendors)
    print(purchasable)

    b = Book(title, description, prices, rating,
             authors, publisher, date, isbn, purchasable, vendors)

    b.display()
    return b


def process_title(title):
    google_api_results = google_books_search_by_title(title)
    num_of_results = google_api_results['totalItems']
    i = 0
    end_i = 5
    results = []
    while(i < end_i and i < num_of_results):
        isbn = google_api_results['items'][i]['volumeInfo']['industryIdentifiers'][0]['identifier']
        general_info = google_api_results['items'][i]['volumeInfo']
        results.append(process_isbn(isbn, general_info))
        i += 1

    return results


def process_api(url):
    response = requests.get(url)
    book_info = json.loads(response.text)

    return book_info


def google_books_search_by_title(title):
    key = "AIzaSyDgszPoXualhFKbDKCNxXXn3cdOhLKgi6A"
    url = r'https://www.googleapis.com/books/v1/volumes?q=title:{}&key={}'.format(
        title, key)
    return process_api(url)


def google_books_search_by_isbn(isbn):
    key = "AIzaSyDgszPoXualhFKbDKCNxXXn3cdOhLKgi6A"

    url = r'https://www.googleapis.com/books/v1/volumes?q=isbn:{}&key={}'.format(
        isbn, key)
    return process_api(url)


def good_book_review(isbn):
    key = "dAZ4wVt4kAgUHeDTPUPDw"
    secret = "ojQMNBUNrFvYrHLDK3cnALRmKQyzDBB3jQw5oGddnY"

    url = r'https://www.goodreads.com/book/review_counts.json?key={}&isbns={}'.format(
        key, isbn)
    response = requests.get(url)
    if response.status_code == 404:
        raise ErrorNoReviewFound
    book_info = json.loads(response.text)
    return book_info

# Book Run API Reference: https://booksrun.com/page/api-reference


def book_run_api_call(isbn):
    price_key = 'hemn2x0o9xwbe7bfz2jz'
    affiliate_key = '5391'

    url = r'https://booksrun.com/api/v3/price/buy/{}?key={}'.format(
        isbn, price_key)

    # url = r'http://booksrun.com/api/price/sell/{}?key={}'.format(isbn, price_key)
    return process_api(url)


# process_title('hunger games')
# result = google_books_search_by_title("hungery games")
# print(result)
# print(result['totalItems'])

# print(result['items'][0]['volumeInfo']['industryIdentifiers'][0]['identifier'])
# print(result['items'][0])
# print(book_run_api_call('1464108730'))
# print(good_book_review('1464108730'))
# print(book_run_api_call('1464108730'))
# print(google_books_search_by_isbn('9780008165130'))
# print(google_books_search_by_title('hunger games'))
process_isbn("9780439023528")
