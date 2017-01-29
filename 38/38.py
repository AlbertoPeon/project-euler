#! /usr/bin/env python3

# https://projecteuler.net/problem=38

from itertools import count

def is_9_pandigital(digits):
    # Ignore 0s
    pandigital = set(digits.replace('0', ''))
    return len(pandigital) == len(digits) and len(pandigital) == 9

largest_pandigital = 0

# We now that the 9 pandigital needs to have 9 digits so any starting number
# needs to have less thant 5, so the simplest combination (which is n * 1 + n * 2)
# won't exceed 9 digits
upper_limit = 10000
for number in range(1, upper_limit):
    for n in range(2, number):
        digits = ''.join(str(number * elem) for elem in range(1, n))
        if len(digits) > 9:
            break
        elif len(digits) != 9:
            continue
        elif is_9_pandigital(digits) and int(digits) > largest_pandigital:
            largest_pandigital = int(digits)

print(largest_pandigital)
