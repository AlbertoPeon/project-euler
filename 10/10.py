import math

N = 2000000

def is_prime(n):
	if n > 2 and n % 2 == 0:
		return False
	for elem in xrange(3, int(math.sqrt(n)) + 1, 2):
		if not n % elem:
			return False
	return True

print sum(n for n in xrange(2, N) if is_prime(n))
