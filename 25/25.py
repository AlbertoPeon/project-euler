from itertools import count
N = 1000

previous_2_N = (1, 1)

for i in count():
	index = i + 3
	value = sum(previous_2_N)
	if len(str(value)) == N:
		print(index)
		break
	previous_2_N = (previous_2_N[1], value)

