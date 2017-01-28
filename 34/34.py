#! /usr/bin/env python3

# https://projecteuler.net/problem=34

from math import factorial

calculate_sum_digit_factorials = lambda number: sum([factorial(int(digit)) for digit in str(number)])

digit_factorials = []
# Exclude 1 and 2 per problem description
# Assume upper limit is 100000
for number in range(3, 100000):
    sum_factorials = calculate_sum_digit_factorials(number)
    if number == sum_factorials:
        print(number)
        digit_factorials.append(number)

print(sum(digit_factorials))
