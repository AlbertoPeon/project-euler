N = 1000

def pythagorean_triplet(N):
	for c in range(int(N / 3),N):
		for b in range(c):
			for a in range(b):
				if a + b + c == N and a ** 2 + b ** 2 == c ** 2:
					return a * b * c

print pythagorean_triplet(N)
