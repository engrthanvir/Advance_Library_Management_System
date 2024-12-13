from datetime import datetime
from lend_return_tracking import log_lend_transaction
from utils import save_data

def get_valid_date(prompt):

    while True:
        date_input = input(prompt).strip()
        if not date_input:
            print("Date cannot be empty. Please enter a valid date.")
            continue
        try:
            due_date = datetime.strptime(date_input, "%Y-%m-%d")
            if due_date < datetime.now():
                print("The due date cannot be in the past. Please enter a valid date.")
                continue
            return due_date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")
            continue

def lend_book(books):

    while True:
        book_title = input("Enter the title of the book to lend (or type 'cancel' to return): ").strip()
        if book_title.lower() == 'cancel':
            print("Action canceled.")
            return
        if not book_title:
            print("Book title cannot be empty. Please try again.")
            continue
        break

    for book in books:
        if book["title"].lower() == book_title.lower():
            if book["quantity"] > book["lent_out"]:
                # Borrower's information
                borrower_name = input("Enter borrower's name: ").strip()
                mobile_number = input("Enter borrower's mobile number: ").strip()

                # Validate mobile number (simple length check for this example)
                while len(mobile_number) != 11 or not mobile_number.isdigit():
                    print("Please enter a valid 11-digit mobile number.")
                    mobile_number = input("Enter borrower's mobile number: ").strip()

                # Due date for return
                due_date = get_valid_date("Enter the return due date (YYYY-MM-DD): ")

                # Update the book's lent out and add borrower information
                book["lent_out"] += 1
                if "borrowers" not in book:
                    book["borrowers"] = []  # If no borrowers list exists, create one.
                book["borrowers"].append({
                    "borrower_name": borrower_name,
                    "mobile_number": mobile_number,
                    "due_date": due_date.strftime("%Y-%m-%d")
                })


                book["quantity"] -= 1

                # Log the lend transaction
                lend_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_lend_transaction(book_title, borrower_name, mobile_number, lend_date, due_date.strftime("%Y-%m-%d"))

                save_data(books)
                print(f"Book '{book_title}' lent out to {borrower_name} successfully. Due date: {due_date.strftime('%Y-%m-%d')}")
            else:
                print(f"All copies of '{book_title}' are currently lent out.")
            return

    print(f"Book '{book_title}' not found.")
