#! /usr/bin/env python3

# https://projecteuler.net/problem=39

from math import sqrt
validate_right_angle_triange = lambda a, b, c:  a ** 2 + b ** 2 == c ** 2

max_p = 1000
max_solutions = set()
final_p = 0
for p in range(1, max_p + 1):
    solutions = set()
    for c in range(1, p):
        # we know a** 2 + b ** 2 = c ** 2
        # and that b = (p - c -a )
        # so expressing b in terms of a
        # a ** 2 + ((p - c) - a) ** 2 = c ** 2
        # which ends as
        # 2a ** 2 - (2 * (p - c)) * a + (p - c) ** 2  - (c ** 2) = 0
        # which is a quadratic equation with values
        quad_a = 2
        quad_b = - (2 * (p - c))
        quad_c = p ** 2  - 2 * p * c
        try:
            # Solving quadratic equation
            a = int((- quad_b + sqrt(quad_b ** 2 - (4 * quad_a * quad_c))) / (2 * quad_a))
            b = p - c - a
            if a > 0 and b > 0 and validate_right_angle_triange(a, b, c):
                # using sets to avoid duplicates
                solutions.add(frozenset([a, b, c]))
        except ValueError:
            # sqrt invalid, skipping
            pass

    if len(solutions) > len(max_solutions):
        max_solutions = solutions
        final_p = p

print(final_p)
