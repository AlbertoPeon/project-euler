#! /usr/bin/env python3

# https://projecteuler.net/problem=50

from itertools import count
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

# Calculate list of primes between 1 and 1000000
primes = []
limit = 1000000
# Obtain accumulated sums
acc_primes = []
sum_primes = 0
for n in count(start=2):
    if n >= limit:
        break
    if is_prime(n):
        sum_primes += n
        primes.append(n)
        acc_primes.append(sum_primes)


consecutive_primes = 1
solution = 0
for i in range(len(acc_primes)):
    for j in range(i - 1, 0, -1):
        n = acc_primes[i] - acc_primes[j]
        if n > limit:
            break
        if i - j > consecutive_primes and is_prime(n):
            consecutive_primes = i - j
            solution = n
            break

print(solution, consecutive_primes)
