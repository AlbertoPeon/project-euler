#! /usr/bin/env python3

# https://projecteuler.net/problem=40

from functools import reduce
from itertools import count
from operator import mul

important_digits = [1, 10, 100, 1000, 10000, 100000, 1000000]

length = 0
result = []
for number in count(start=1):
    str_number = str(number)
    if length < important_digits[0] and length + len(str_number) >= important_digits[0]:
        result.append(int(str_number[important_digits.pop(0) - length - 1]))

    if not important_digits:
        break

    length += len(str_number)

print(reduce(mul, result, 1))
