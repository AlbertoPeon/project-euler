#! /usr/bin/env python3

# https://projecteuler.net/problem=35
from math import sqrt

def circulate_number(number):
    str_number = str(number)
    for n in range(len(str_number)):
        yield int(str_number[n:len(str_number)] + str_number[0:n])

def is_prime(n):
    if n < 0:
        return False
    if n > 2 and n % 2 == 0:
        return False
    for elem in range(3, int(sqrt(n)) + 1, 2):
        if not n % elem:
            return False
    return True

upper_limit = 1000000
circular_primes=set()

for number in range(2, upper_limit):
    for combination in circulate_number(number):
        if len(str(combination)) != len(str(number)) or not is_prime(combination):
            break
    else:
        circular_primes.add(number)

print(len(circular_primes))
