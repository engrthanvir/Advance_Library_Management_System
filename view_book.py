def view_books(books):

    if not books:
        print("No books available in the library.")
        return

    print("\nList of Books in the Library:")
    print(f"{'Title':<30} {'Author':<20} {'Year':<6} {'Quantity':<8} {'ISBN':<15} {'Added At':<20} {'Last Updated':<20}")
    print("-" * 120)

    for book in books:
        title = book["title"]
        author = book["author"]
        year = book["year"]
        quantity = book["quantity"]
        isbn = book["isbn"]
        added_at = book["book_at_add"]
        last_updated = book["book_at_update"] if book["book_at_update"] else "Not Updated"

        print(f"{title:<30} {author:<20} {year:<6} {quantity:<8} {isbn:<15} {added_at:<20} {last_updated:<20}")
