import pytest
from book import Book
from library import Library

@pytest.fixture
def library():
    lib = Library()
    lib.add_user('Tovi')
    return lib

def test_add_book(library):
    book = Book('Leishaer Yehudi','Rav Itzchak Zilber')
    library.add_book(book)
    assert book in library.books

def test_add_user(library):
    library.add_user('Tovi Kuperman')
    assert 'Tovi Kuperman' in library.users

def test_check_out_book(library):
    user_name='Ayala Kuperman'
    library.add_user(user_name)
    book = Book('Bachatzi Halayla', 'Chaim Greenboim')
    library.add_book(book)
    library.check_out_book(user_name, book)
    assert book.is_checked_out is True
    assert library.checked_out_books[user_name] == book

def test_return_book(library):
    user_name='Ayala Kuperman'
    library.add_user(user_name)
    book = Book('Bachatzi Halayla', 'Chaim Greenboim')
    library.add_book(book)
    library.check_out_book(user_name, book)
    assert book not in library.books
    assert book.is_checked_out is False

def test_search_books(library):

    #המשך יבוא