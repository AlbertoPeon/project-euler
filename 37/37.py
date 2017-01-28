#! /usr/bin/env python3

# https://projecteuler.net/problem=37

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

def truncate(number, reverse=False):
    str_number = str(number)
    for n in range(len(str_number)):
        if reverse:
            yield int(str_number[:len(str_number) - n])
        else:
            yield int(str_number[n:])

def is_truncable_prime(number, reverse=False):
    for n in truncate(number, reverse):
        if not is_prime(n):
            return False
    return True

truncable_primes = set()

for n in count(start=10):
    if is_prime(n) and is_truncable_prime(n) and is_truncable_prime(n, reverse=True):
        truncable_primes.add(n)

    # We know there are only 11 prime numbers
    if len(truncable_primes) == 11:
        print(sum(truncable_primes))
        break
