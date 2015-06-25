N = 10000

MAP = {}

def calculate_divisors(number):
    result = {1}
    for n in range(2, int(number/2) + 1):
        if number % n == 0:
            result.add(n)
    return result

def d(number):
    if number not in MAP:
        MAP[number] = sum(calculate_divisors(number))
    return MAP[number]

def are_amicable_pair(a, b):
    return d(a) == b and d(b) == a and a != b

amicable_numbers = set()

for a in range(1, N):
    for b in range(a + 1, N):
        if are_amicable_pair(a,b):
            amicable_numbers.add(a)
            amicable_numbers.add(b)

print(sum(amicable_numbers))