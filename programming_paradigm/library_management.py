"""
library_management.py
A simple system to manage books in a library using OOP principles.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Private attribute to track if the book is checked out.
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        # Private list to store Book objects.
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {book.title}")
                    return
                else:
                    print(f"'{book.title}' is already checked out.")
                    return
        print(f"Error: '{title}' not found in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {book.title}")
                    return
                else:
                    print(f"'{book.title}' is already in the library.")
                    return
        print(f"Error: '{title}' not found in the library.")

    def list_available_books(self):
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(book)
                available_count += 1
        if available_count == 0:
            print("No books are currently available.")