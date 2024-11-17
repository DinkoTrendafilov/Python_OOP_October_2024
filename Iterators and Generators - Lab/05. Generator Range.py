def genrange(start: int, end: int):
    return (i for i in range(start, end + 1))


print(list(genrange(1, 10)))
print()
print(list(genrange(5, 15)))
