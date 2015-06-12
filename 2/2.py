import itertools
MAX = 4000000

total = 2
previous = (1, 2)
for n in itertools.count():
    value = sum(previous)
    previous = (previous[1], value)
    if value > MAX:
        break
    if not value % 2:
        total += value

print total
