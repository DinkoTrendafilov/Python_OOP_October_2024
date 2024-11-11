numbers = [int(x) for x in input().split()]

numbers.sort()
mid = numbers[len(numbers) // 2]
before_mid = numbers[len(numbers) // 2 - 1]
avg = sum(numbers) / len(numbers)
print(*sorted(numbers), sep=", ")
print(f"Sum: {sum(numbers)}")
print(f"Length: {len(numbers)}")
print(f"Average: {avg}")
print(f"Clear digits of AVG: {len([x for x in str(avg) if x != '.']) - len(str(int(avg)))}")
print(f"Total digits of AVG: {len(str(avg))}")
if len(numbers) % 2 == 1:
    print(f"Middle element: {mid} - index: {numbers.index(mid)}")
else:
    print(f"Middle elements: {mid}, {numbers[len(numbers) // 2 - 1]}")



