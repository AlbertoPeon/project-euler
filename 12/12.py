from itertools import count
from math import sqrt

MAX_DIVISORS = 500

def calculate_n_divisors(number):
    result = 0
    for n in range(1, int(sqrt(number)) + 1):
        if float(n) == sqrt(number):
            result += 1
        elif number % n == 0:
            result += 2
    return result

def triangular_numbers():
    value = 0
    for n in count():
        value += n
        yield value

for number in triangular_numbers():
    divisors = calculate_n_divisors(number)
    if divisors > MAX_DIVISORS:
        print('Found it! Number is {0} and has {1} divisors'.format(number, divisors))
        break
