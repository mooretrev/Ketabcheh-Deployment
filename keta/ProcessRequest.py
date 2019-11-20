import requests
import json

'''
    Book Run API Reference: https://booksrun.com/page/api-reference
'''
######## OLIN
def process_isbn(isbn):
    # create book data structure
    pass

def process_title(title):
    # create an array of book data structure
    pass

def process_api(url):
    response = requests.get(url)
    book_info = json.loads(response.text)

    return book_info

def google_books_search_by_title(title):
    key = "AIzaSyDgszPoXualhFKbDKCNxXXn3cdOhLKgi6A"
    url = r'https://www.googleapis.com/books/v1/volumes?q=title:{}&key={}'.format(title, key)
    return process_api(url)

def google_books_search_by_isbn(isbn):
    key = "AIzaSyDgszPoXualhFKbDKCNxXXn3cdOhLKgi6A"

    url = r'https://www.googleapis.com/books/v1/volumes?q=isbn:{}&key={}'.format(isbn, key)
    return process_api(url)

def good_book_review(isbn):
    key = "dAZ4wVt4kAgUHeDTPUPDw"
    secret = "ojQMNBUNrFvYrHLDK3cnALRmKQyzDBB3jQw5oGddnY"

    url = r'https://www.goodreads.com/book/review_counts.json?key={}&isbns={}'.format(key, isbn)
    return process_api(url)

# Book Run API Reference: https://booksrun.com/page/api-reference
def book_run_api_call(isbn):
    price_key = 'hemn2x0o9xwbe7bfz2jz'
    affiliate_key = '5391'

    url = r'https://booksrun.com/api/v3/price/buy/{}?key={}'.format(isbn, price_key)


    # url = r'http://booksrun.com/api/price/sell/{}?key={}'.format(isbn, price_key)
    return process_api(url)



# result = books_search_by_title("hungery games")
# print(result)
# print(result['items'][0])

# print(book_run_api_call('1464108730'))
# print(good_book_review('1464108730'))
print(book_run_api_call('1464108730'))
# print(google_books_search_by_isbn('1464108730'))



