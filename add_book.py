import random
from datetime import datetime
from utils import save_data

def get_valid_integer(prompt):
    """Helper function to get a valid integer from the user."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be empty. Please enter a value.")
            continue
        try:
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def add_book(books):
    """Add a new book to the library."""
    while True:
        title = input("Enter the title of the book (or type 'cancel' to return): ").strip()
        if title.lower() == 'cancel':
            print("Action canceled.")
            return
        if not title:
            print("Book title cannot be empty. Please try again.")
            continue
        break

    while True:
        author = input("Enter the author of the book (or type 'cancel' to return): ").strip()
        if author.lower() == 'cancel':
            print("Action canceled.")
            return
        if not author:
            print("Author name cannot be empty. Please try again.")
            continue
        break

    year = get_valid_integer("Enter the publication year: ")
    quantity = get_valid_integer("Enter the quantity of the book: ")

    isbn = str(random.randint(1000000000000, 9999999999999))  # Generate random 13-digit ISBN
    book = {
        "title": title,
        "author": author,
        "year": year,
        "quantity": quantity,
        "lent_out": 0,  # Number of books lent out
        "isbn": isbn,
        "book_at_add": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Timestamp when the book was added
        "book_at_update": None  # Set to None initially, as the book is not updated yet
    }
    books.append(book)
    save_data(books)
    print(f"Book '{title}' by {author} added successfully.")
