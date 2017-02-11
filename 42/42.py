#! /usr/bin/env python3

# https://projecteuler.net/problem=42

from math import sqrt
import csv

# We want to reverse the equation to solve 'n' instead of 'tn'
# tn = 1/2 * n * (n-1)
# which is a quadratic equation
# n ** 2 + n - 2tn = 0

# Solving quadratic equation - the result must be a whole integer instead of a float
is_triangle_number = lambda tn: ((-1 + sqrt((-1) ** 2 - (4 * ((-2) * tn)))) / 2).is_integer()

alphabetic_value = lambda char: ord(char) - ord('A') + 1

# Import all words
with open('p042_words.txt') as csvfile:
    for reader in csv.reader(csvfile, delimiter=','):
        words = reader

triangle_words = 0
for word in words:
    value = sum(map(alphabetic_value, word))
    if is_triangle_number(value):
        triangle_words += 1

print(triangle_words)
