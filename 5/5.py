
NUMBERS = range(20, 0, -1) 

def smallest_multiple(numbers):
	max_limit = reduce(lambda n1, n2: n1 * n2, numbers)
	for result in xrange(20, max_limit):
		for n in NUMBERS:
			if result % n:
				break
		else:
			return result

print smallest_multiple(NUMBERS)