N = 100

def sum_of_squares(n):
	return sum(map(lambda n: n ** 2, xrange(n + 1)))

def square_of_sums(n):
	return sum(xrange(n + 1)) ** 2

print square_of_sums(N) - sum_of_squares(N)