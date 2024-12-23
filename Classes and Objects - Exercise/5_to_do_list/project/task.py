from typing import List


class Task:
    def __init__(self, name: str, due_date: str) -> None:
        self.name = name
        self.due_date = due_date
        self.comments: List[str] = []
        self.completed = False

    def change_name(self, new_name: str) -> str:
        if self.name == new_name:
            return "Name cannot be the same."

        self.name = new_name
        return self.name

    def change_due_date(self, new_data: str) -> str:
        if self.due_date == new_data:
            return "Date cannot be the same."

        self.due_date = new_data
        return self.due_date

    def add_comment(self, comment: str) -> None:
        self.comments.append(comment)

    def edit_comment(self, comment_index: int, new_comment: str) -> str or None:
        if not  0 <= comment_index < len(self.comments):
            return "Cannot find comment."
        else:
            self.comments[comment_index] = new_comment
            result = ", ".join(self.comments)
            return result

    def details(self) -> str:
        return f"Name: {self.name} - Due Date: {self.due_date}"
