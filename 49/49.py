#! /usr/bin/env python3

# https://projecteuler.net/problem=49

from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n > 2 and n % 2 == 0:
        return False
    for elem in range(3, int(sqrt(n)) + 1, 2):
        if not n % elem:
            return False
    return True

sequence = lambda n: [str(s) for s in [n, n + 3330, n + 3330 * 2]]

for n in range(1000, 10000 - 3330 * 2):
    seq = sequence(n)
    if len(set(''.join(sorted(n)) for n in sequence(n))) == 1:
        if not False in map(is_prime, map(int, seq)):
            print(''.join(seq))
