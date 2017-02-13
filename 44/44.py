#! /usr/bin/env python3

from math import sqrt

# https://projecteuler.net/problem=44
pentagon_number = lambda n: int((n * (3 * n - 1)) / 2)

# We also need the inverse of this function, which is, once again, a quadratic function
# 2p = n * (3*n - 1)
# 0 = 3*n**2 - 1n - 2p

is_pentagon_number = lambda p: ((1 + sqrt(((-1) ** 2) - (4 * 3 * (-2 * p)))) / (2 * 3)).is_integer()

def gen_pentagon_number(start, top):
    for n in range(start, top):
        yield n, pentagon_number(n)

top=10000
min_d = None
for j, val_j in gen_pentagon_number(1, top):
    if min_d:
        break
    for k, val_k in gen_pentagon_number(j, top):
        if is_pentagon_number(val_k + val_j) and is_pentagon_number(val_k - val_j):
            if not min_d or val_k - val_j < min_d:
                min_d = val_k - val_j
                break

print(min_d)
