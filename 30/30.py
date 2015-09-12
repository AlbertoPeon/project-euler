
power = 5

MAX = 1000000

selected = set()
for number in range(2, MAX):
    if number == sum(list(map(lambda n: int(n) ** power, str(number)))):
        selected.add(number)

print(sum(selected))
