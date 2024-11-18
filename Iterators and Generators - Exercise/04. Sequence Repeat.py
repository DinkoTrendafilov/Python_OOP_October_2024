class sequence_repeat:
    def __init__(self, sequence, repeat_count):
        self.sequence = sequence
        self.repeat_count = repeat_count
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.repeat_count:
            char = self.sequence[self.i % len(self.sequence)]
            self.i += 1
            return char
        else:
            raise StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
print()
print()
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
