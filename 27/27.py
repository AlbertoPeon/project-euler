from functools import reduce
from operator import mul
from math import sqrt

d = 1000

def quadratic_form(a, b, n):
    return (n ** 2) + (a * n) + b


def is_prime(n):
    if n < 0:
        return False
    if n > 2 and n % 2 == 0:
        return False
    for elem in range(3, int(sqrt(n)) + 1, 2):
        if not n % elem:
            return False
    return True

max_a_b = (0, 0)
max_n = 0

for a in range(1-d, d):
    for b in range(1-d, d):
        n = 0
        while True:
            if not is_prime(quadratic_form(a, b, n)):
                if n > max_n:
                    max_n = n
                    max_a_b = a, b
                break
            n+=1

print("a = '%s', b = '%s' and their product is '%s'. Max number of consecutives primes is"
    " '%s'" % (max_a_b + (reduce(mul, max_a_b), max_n)))