import json

def load_data():

    try:
        with open('books.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist

def save_data(books):
    """Save the book data to a JSON file."""
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)
