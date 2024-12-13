import json
from datetime import datetime

def load_lend_return_data():

    try:
        with open('lend_return_log.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

def save_lend_return_data(logs):

    with open('lend_return_log.json', 'w') as file:
        json.dump(logs, file, indent=4)

def log_lend_transaction(book_title, borrower_name, mobile_number, lend_date, due_date):
    """Log a lend transaction."""
    logs = load_lend_return_data()
    lend_entry = {
        "book_title": book_title,
        "borrower_name": borrower_name,
        "mobile_number": mobile_number,
        "lend_date": lend_date,
        "due_date": due_date,
        "return_date": None
    }
    logs.append(lend_entry)
    save_lend_return_data(logs)

def log_return_transaction(book_title, borrower_name, mobile_number, return_date):

    logs = load_lend_return_data()
    for entry in logs:
        if entry["book_title"] == book_title and entry["borrower_name"] == borrower_name and entry["mobile_number"] == mobile_number and entry["return_date"] is None:
            entry["return_date"] = return_date  # Update the return date
            break
    save_lend_return_data(logs)
