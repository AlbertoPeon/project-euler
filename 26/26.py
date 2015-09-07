
d = 1000

def recurrent_cycle(n):
    for r in range(1, n):
        if 10 ** r % n == 1:
            return r
    return 0

print("The number with the longest recurrent cycle is '%s' ('%s')" % 
    max([(i, recurrent_cycle(i)) for i in range(2, d)],
        key=lambda tup: tup[-1]))