MAX = 1000000

def collatz_fuction(number):
    size = 1
    while number > 1:
        if number % 2 == 0:
            number = int(number / 2)
        else:
            number = 3 * number + 1
        size += 1
    return size

result = (0, 0)
for n in range(1, MAX):
    size = collatz_fuction(n)
    if result[1] < size:
        result = (n, size)
else:
    print('The longest chain is {1}, starting number: {0}'.format(*result))