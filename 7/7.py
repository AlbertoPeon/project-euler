from sys import maxint

N = 10001

pos = 2
def is_prime(n):
	for elem in xrange(2, n):
		if not n % elem:
			return False
	return True

# Only odd numbers starting with 3
for x in xrange(3, maxint, 2):
	if is_prime(x):
		print x
		if pos == N:
			print x
			break
		pos += 1

		