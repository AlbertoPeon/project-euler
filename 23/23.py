from math import sqrt
from itertools import combinations_with_replacement

def proper_divisors(number):
    result = {1}
    for n in range(2, int(sqrt(number)) + 1):
        if number % n == 0:
            result.add(n)
            if n != int(number / n):
                result.add(int(number / n))
    return result

is_abundant = lambda number: sum(proper_divisors(number)) > number

abundant_numbers = []
for number in range(1, 28124):
	if is_abundant(number):
		abundant_numbers.append(number)

non_numbers = set(map(sum, combinations_with_replacement(abundant_numbers, 2)))

print(sum([number for number in range(1, 28124) if number not in non_numbers]))