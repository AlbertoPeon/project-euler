"""

Regardless of which route is taken, to reach the bottom-left point, we have to
move 20 times to the right and 20 times down. Always.

Therefore, the problem can be seen as finding all the permutations of a 2 elements set [right, down]
with size 20 + 20 = 40

which, by definition, translates to:

40! / (20! + 20!)

"""
from math import factorial

N = 20
result = int(factorial(N + N) / (factorial(N) * factorial(N)))

print('Number of possible routes in a {0}x{0} grid : {1}'.format(N, result))