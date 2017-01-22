#! /usr/bin/env python3

# https://projecteuler.net/problem=33

from fractions import Fraction
from functools import reduce
from operator import mul

def cancel_fraction(numerator, denominator):
    """Remove same number from numerator and denominator """
    str_numerator, str_denominator = str(numerator), str(denominator)

    for digit in str_numerator:
        # Ignore '0's
        if digit in str_denominator and digit != '0':
            str_numerator = str_numerator.replace(digit, '')
            str_denominator = str_denominator.replace(digit, '')
            # Unless any number is empty or the denominator is '0'...
            if str_numerator and str_denominator and str_denominator != '0':
                return int(str_numerator), int(str_denominator)
    return numerator, denominator

def digit_cancelling_fractions():
    fractions = []
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            red_numerator, red_denominator = cancel_fraction(numerator, denominator)
            red_fraction = Fraction(red_numerator, red_denominator)
            if numerator != red_numerator and Fraction(numerator, denominator) == red_fraction:
                fractions.append(red_fraction)
    return reduce(mul, fractions, 1).denominator

print(digit_cancelling_fractions())
