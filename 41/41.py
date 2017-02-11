#! /usr/bin/env python3

# https://projecteuler.net/problem=41

from math import sqrt
from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    if n > 2 and n % 2 == 0:
        return False
    for elem in range(3, int(sqrt(n)) + 1, 2):
        if not n % elem:
            return False
    return True

largest = 0
for n in reversed(range(1, 10)):
    # Generate permutations of all number
    for perm in permutations(range(1,n + 1)):
        n = int(''.join(map(str, perm)))
        if is_prime(n) and n > largest:
            largest = n
    if largest != 0:
        break

print(largest)
