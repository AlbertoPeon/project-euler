#! /usr/bin/env python3

# https://projecteuler.net/problem=43

from itertools import permutations

result = 0
divisors = [2, 3, 5, 7, 11, 13, 17]

for number in permutations(map(str,range(0,10))):
    for index, divisor in enumerate(divisors):
        if int(''.join(number[index+1:index+4])) % divisor != 0:
            break
    else:
        result += int(''.join(number))

print(result)
