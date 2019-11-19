import requests
import json

'''
    Given an isbn number, return an array of the related info about the book
    
    Use json loads
'''
def books_search_by_title(title):
    key = "AIzaSyDgszPoXualhFKbDKCNxXXn3cdOhLKgi6A"

    url = r'https://www.googleapis.com/books/v1/volumes?q=title:{}&key={}'.format(title, key)
    response = requests.get(url)
    book_info = json.loads(response.text)

    return book_info

def books_search_by_isbn(isbn):
    key = "AIzaSyDgszPoXualhFKbDKCNxXXn3cdOhLKgi6A"

    url = r'https://www.googleapis.com/books/v1/volumes?q=isbn:{}&key={}'.format(isbn, key)
    response = requests.get(url)
    book_info = json.loads(response.text)

    return book_info


result = books_search_by_title("hungery games")
print(result)
# print(result['items'][0])





