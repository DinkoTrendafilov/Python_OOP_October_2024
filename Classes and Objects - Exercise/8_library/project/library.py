from project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if book_name in self.books_available.get(author, []):
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        elif user.username in self.rented_books and book_name in self.rented_books[user.username]:
            days_remaining = self.rented_books[user.username][book_name]
            return f'The book "{book_name}" is already rented and will be available in {days_remaining} days!'
        return f'The book "{book_name}" is already rented and unavailable.'

    def return_book(self, author: str, book_name: str, user: User) -> str:
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available.setdefault(author, []).append(book_name)
            if user.username in self.rented_books:
                self.rented_books[user.username].pop(book_name, None)
                if not self.rented_books[user.username]:
                    self.rented_books.pop(user.username)
        else:
            return f"{user.username} doesn't have this book in his/her records!"
