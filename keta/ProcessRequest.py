import requests
import json

'''
    Given an isbn number, return an array of the related info about the book
    
    Use json loads
'''
def process_api(url):
    response = requests.get(url)
    book_info = json.loads(response.text)

    return book_info

def books_search_by_title(title):
    key = "AIzaSyDgszPoXualhFKbDKCNxXXn3cdOhLKgi6A"
    url = r'https://www.googleapis.com/books/v1/volumes?q=title:{}&key={}'.format(title, key)
    return process_api(url)

def books_search_by_isbn(isbn):
    key = "AIzaSyDgszPoXualhFKbDKCNxXXn3cdOhLKgi6A"

    url = r'https://www.googleapis.com/books/v1/volumes?q=isbn:{}&key={}'.format(isbn, key)
    return process_api(url)

def book_run_api_call(isbn):
    price_key = 'hemn2x0o9xwbe7bfz2jz'
    affiliate_key = '5391'

    url = r'http://booksrun.com/api/price/sell/{}?key={}'.format(isbn, price_key)
    return process_api(url)



# result = books_search_by_title("hungery games")
# print(result)
# print(result['items'][0])

print(book_run_api_call('1464108730'))





