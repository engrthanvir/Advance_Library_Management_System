from utils import save_data


def delete_book(books):

    title = input("Enter the title of the book to delete: ").strip()

    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            save_data(books)
            print(f"Book '{title}' deleted successfully.")
            return
    print(f"Book '{title}' not found.")
