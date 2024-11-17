def squares(num):
    return (i ** 2 for i in range(1, num + 1))


print(list(squares(5)))
