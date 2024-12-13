import sys
from utils import load_data
from add_book import add_book
from delete_book import delete_book
from update_book import update_book
from lend_book import lend_book
from return_book import return_book
from view_book import view_books


def menu():

    books = load_data()

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Delete a book")
        print("3. Update book details")
        print("4. View books")
        print("5. Lend a book")
        print("6. Return a book")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(books)
        elif choice == "2":
            delete_book(books)
        elif choice == "3":
            update_book(books)
        elif choice == "4":
            view_books(books)
        elif choice == "5":
            lend_book(books)
        elif choice == "6":
            return_book(books)
        elif choice == "7":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()