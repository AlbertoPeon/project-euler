#! /usr/bin/env python3

# https://projecteuler.net/problem=46

from math import sqrt
from itertools import count

def is_prime(n):
    if n <= 1:
        return False
    if n > 2 and n % 2 == 0:
        return False
    for elem in range(3, int(sqrt(n)) + 1, 2):
        if not n % elem:
            return False
    return True

def theorem_matches(n):
    for power in count(start=1):
        if 2 * power ** 2 >= n:
            return False
        if is_prime(n - (2 * power ** 2)):
            return True

# All odd numbers
for n in count(start=3, step=2):
    if not is_prime(n):
        if not theorem_matches(n):
            print(n)
            break
