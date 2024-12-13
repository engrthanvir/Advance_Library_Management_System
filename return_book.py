from datetime import datetime
from lend_return_tracking import log_return_transaction
from utils import save_data

def return_book(books):
    """Return a lent book to the library."""
    while True:
        book_title = input("Enter the title of the book to return (or type 'cancel' to return): ").strip()
        if book_title.lower() == 'cancel':
            print("Action canceled.")
            return
        if not book_title:
            print("Book title cannot be empty. Please try again.")
            continue
        break

    for book in books:
        if book["title"].lower() == book_title.lower():
            if "borrowers" in book and book["borrowers"]:
                print(f"Returning book '{book_title}':")
                # List the borrowers and allow user to select by number
                for i, borrower in enumerate(book["borrowers"], 1):
                    print(f"{i}. {borrower['borrower_name']} - Due Date: {borrower['due_date']}")

                while True:
                    borrower_choice = input("Enter the borrower number to return the book (or 'cancel' to return): ").strip()
                    if borrower_choice.lower() == 'cancel':
                        print("Action canceled.")
                        return
                    try:
                        borrower_choice = int(borrower_choice)
                        # Check if borrower number is valid
                        if borrower_choice < 1 or borrower_choice > len(book["borrowers"]):
                            print("Invalid choice. Please select a valid borrower number.")
                            continue
                        break  # Exit loop if input is valid
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                # Remove borrower from the list
                borrower = book["borrowers"].pop(borrower_choice - 1)

                # Update the book's quantity and lent-out count
                book["lent_out"] -= 1
                book["quantity"] += 1

                # Record the return date
                return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Book '{book_title}' returned successfully on {return_date}.")
                print(f"Borrower's details: {borrower['borrower_name']}, {borrower['mobile_number']}, Due Date: {borrower['due_date']}")

                # Log the return transaction
                log_return_transaction(book_title, borrower["borrower_name"], borrower["mobile_number"], return_date)

                # Save the updated book data
                save_data(books)
            else:
                print(f"No copies of '{book_title}' are currently lent out.")
            return

    print(f"Book '{book_title}' not found.")
