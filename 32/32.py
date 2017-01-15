#! /usr/bin/env python3

# https://projecteuler.net/problem=32

from itertools import count

def is_9_pandigital(numbers):
    # Ignore Xs
    return 9 == len(set(numbers.replace('X', '')))

def calculate_sum_pandigital_numbers():
    pandigitals = set()
    for multiplicand in count():
        for multiplier in count(start=multiplicand):
            product = multiplicand * multiplier

            # Replace 0s for Xs to ensure they don't count
            numbers = ''.join(map(str, (multiplicand, multiplier, product))).replace('0', 'X')

            if len(numbers) == 9:
                if is_9_pandigital(numbers):
                    pandigitals.add(product)
            elif len(numbers) > 9:
                if multiplier == multiplicand:
                    # If it is the first iteration return. There is no way following
                    # numbers will be smaller
                    return sum(pandigitals)
                else:
                    # Jump to next loop as this one will always be bigger
                    break
            else:
                pass

print(calculate_sum_pandigital_numbers())
