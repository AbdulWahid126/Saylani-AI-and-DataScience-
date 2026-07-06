class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False
        
    def __str__(self):
        return f"{self.title} by {self.author} (ID: {self.book_id}) - Available: {self.available_copies}/{self.total_copies}"

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []  # List of book IDs

    def borrow_book(self, book_id):
        self.borrowed_books.append(book_id)

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False

class Library:
    def __init__(self):
        self.books = {}  # book_id: Book
        self.users = {}  # user_id: User

    def add_book(self, book_id, title, author, total_copies):
        if book_id in self.books:
            return False, "Book ID already exists."
        new_book = Book(book_id, title, author, total_copies)
        self.books[book_id] = new_book
        return True, "Book added successfully."

    def add_user(self, user_id, name):
        if user_id in self.users:
            return False, "User ID already exists."
        new_user = User(user_id, name)
        self.users[user_id] = new_user
        return True, "User registered successfully."

    def search_by_title(self, title):
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        return results

    def search_by_author(self, author):
        results = [book for book in self.books.values() if author.lower() in book.author.lower()]
        return results

    def borrow_book(self, user_id, book_id):
        if user_id not in self.users:
            return False, "User not found."
        if book_id not in self.books:
            return False, "Book not found."

        user = self.users[user_id]
        book = self.books[book_id]

        if book_id in user.borrowed_books:
            return False, "User has already borrowed this book."

        if book.borrow():
            user.borrow_book(book_id)
            return True, f"Successfully borrowed '{book.title}'."
        else:
            return False, f"Sorry, no available copies of '{book.title}'."

    def return_book(self, user_id, book_id):
        if user_id not in self.users:
            return False, "User not found."
        if book_id not in self.books:
            return False, "Book not found."

        user = self.users[user_id]
        book = self.books[book_id]

        if book_id not in user.borrowed_books:
            return False, "User has not borrowed this book."

        if book.return_book():
            user.return_book(book_id)
            return True, f"Successfully returned '{book.title}'."
        else:
            return False, "Error returning book."

    def view_all_books(self):
        return list(self.books.values())
        
    def check_availability(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            return True, f"'{book.title}' has {book.available_copies} copies available."
        return False, "Book not found."
