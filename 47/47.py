#! /usr/bin/env python3

# https://projecteuler.net/problem=47

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

def has_n_prime_factors(number, n):
    factors = set()
    for factor in range(2, int(sqrt(number)) + 1):
        if number % factor == 0:
            if is_prime(factor):
                factors.add(factor)
            other = int(number/factor)
            if is_prime(other):
                factors.add(other)
    return len(factors) == n

MAX_CONSECUTIVE = 4

consecutive = 0
#for n in count(start=647):
for n in count():
    if has_n_prime_factors(n, MAX_CONSECUTIVE):
        consecutive += 1
        if consecutive == MAX_CONSECUTIVE:
            print(list(range(n - MAX_CONSECUTIVE + 1, n + 1)))
            break
    else:
        consecutive = 0
