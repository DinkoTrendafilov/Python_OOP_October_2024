class Stack:
    def __init__(self, *args):
        self.data = list(args)

    def push(self, element: str) -> None:
        if isinstance(element, str):
            self.data.append(element)

    def pop(self) -> str or None:
        if not self.is_empty():
            return self.data.pop()

    def top(self) -> str or None:
        if not self.is_empty():
            return self.data[-1]

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def __str__(self) -> str:
        return "[" + ", ".join(reversed(self.data)) + "]"


stack = Stack()
stack.push("apple")
stack.push("banana")
stack.push("cherry")
print(stack)
print(stack.pop())
print(stack)
print(stack.top())
print(stack.is_empty())
