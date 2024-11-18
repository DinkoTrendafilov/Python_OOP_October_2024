def possible_permutations(numbers):
    if len(numbers) == 0:
        yield []
    else:
        for i in range(len(numbers)):
            for p in possible_permutations(numbers[:i] + numbers[i + 1:]):
                yield [numbers[i]] + p


[print(n) for n in possible_permutations([1, 2, 3])]
print()
print()
[print(n) for n in possible_permutations([1])]
