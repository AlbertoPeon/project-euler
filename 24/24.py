from itertools import permutations

NUMBERS = range(10)

INDEX = 1000000

print(''.join(str(elem) for elem in list(permutations(NUMBERS))[INDEX - 1]))
