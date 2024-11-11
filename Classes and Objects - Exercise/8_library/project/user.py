class User:
    def __init__(self, user_id: int, username: str) -> None:
        self.user_id = user_id
        self.username = username
        self.books: list[str] = []

    def info(self) -> str:
        books = ", ".join(sorted(self.books))
        return books

    def __str__(self) -> str:
        return f"{self.user_id}, {self.username}, {self.books}"
