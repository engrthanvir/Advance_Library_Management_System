from datetime import datetime

from utils import save_data

def update_book(books):

    title = input("Enter the title of the book to update: ").strip()

    for book in books:
        if book["title"].lower() == title.lower():
            new_title = input(f"Enter new title (leave blank to keep '{book['title']}'): ").strip()
            if new_title:
                book["title"] = new_title

            new_author = input(f"Enter new author (leave blank to keep '{book['author']}'): ").strip()
            if new_author:
                book["author"] = new_author

            new_year = input(f"Enter new year (leave blank to keep '{book['year']}'): ").strip()
            if new_year:
                book["year"] = new_year

            new_quantity = input(f"Enter new quantity (leave blank to keep '{book['quantity']}'): ").strip()
            if new_quantity:
                book["quantity"] = int(new_quantity)

            book["book_at_update"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_data(books)
            print(f"Book '{title}' updated successfully.")
            return

    print(f"Book '{title}' not found.")
