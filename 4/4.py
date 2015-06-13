

max_palindrome = 0
is_palindrome = lambda n: str(n) == str(n)[::-1]

for i in xrange(100, 1000):
	for j in xrange(100, 1000):
		product = i * j
		if is_palindrome(product) and product > max_palindrome:
			max_palindrome = product

print max_palindrome
