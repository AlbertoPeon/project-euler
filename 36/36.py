#! /usr/bin/env python3

# https://projecteuler.net/problem=36

is_palindrome = lambda s: s == s[::-1]

upper_limit = 1000000
double_base_palindromes = set()

for number in range(upper_limit):
    decimal = str(number)
    binary = "{0:b}".format(number)
    if is_palindrome(decimal) and is_palindrome(binary):
        double_base_palindromes.add(number)

print(sum(double_base_palindromes))
