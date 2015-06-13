N = 600851475143

is_factor = lambda n, factor: not n % factor 

def max_prime_factor(number):
	max_factor = 0
	current_factor = 2
	while number > 1:
		while is_factor(number, current_factor):
			number /= current_factor
			max_factor = current_factor
		current_factor += 1
	return max_factor

print max_prime_factor(N)