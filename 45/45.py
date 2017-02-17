#! /usr/bin/env python3

from math import sqrt
from itertools import count

# https://projecteuler.net/problem=45

solve_quadratic_equation = lambda a, b, c: (((-b) + sqrt((b) ** 2 - (4 * a * c))) / (2 * a))

calculate_triangle = lambda n: int((n * (n + 1)) / 2)
# Triangle
# n ** 2 + 1n - 2t = 0
is_triangle = lambda t: solve_quadratic_equation(1, 1, -2 * t).is_integer()

# Pentagonal (from exercise 44)
# 0 = 3*n**2 - 1n - 2p
is_pentagonal = lambda p: solve_quadratic_equation(3, -1, -2 * p).is_integer()

# Hexagonal
# 2n ** 2 -1n - h = 0
is_hexagonal = lambda h: solve_quadratic_equation(2, -1, -h).is_integer()

start=285
for n in count(start=285 + 1):
    n_triangle = calculate_triangle(n)
    if is_pentagonal(n_triangle) and is_hexagonal(n_triangle):
        print(n_triangle)
        break
