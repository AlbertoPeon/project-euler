
with open('22/names.txt', 'r') as names_file:
	names = sorted(names_file.read().replace('"', '').split(','))

get_alphabetical_pos = lambda char: ord(char) - ord('A') + 1

compute_score = lambda name: sum(map(get_alphabetical_pos, name)) * (names.index(name) + 1)

print(sum(map(compute_score, names)))