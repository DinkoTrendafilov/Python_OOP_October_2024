n = int(input())


def print_top_part(number):
    for row in range(1, number + 1):
        print(f"{' ' * (number - row)}{'* ' * row}")


def print_bottom_part(number):
    for row in range(number - 1, 0, -1):
        print(f"{' ' * (number - row)}{'* ' * row}")


print_top_part(n)
print_bottom_part(n)
