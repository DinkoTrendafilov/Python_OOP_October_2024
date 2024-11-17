class take_skip:
    def __init__(self, step: int, count: int) -> None:
        self.step = step
        self.count = count
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.count:
            value = self.i * self.step
            self.i += 1
            return value
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
print()
numbers = take_skip(10, 5)
for number in numbers:
    print(number)
