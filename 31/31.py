
VALUE = 200

COINS = [1, 2, 5, 10, 20, 50, 100, 200]

def find_combinations(remaining=VALUE, coins=COINS):
	if remaining == 0:
		return 1
	if coins and remaining > 0:
		return find_combinations(remaining - coins[0], coins) + find_combinations(remaining, coins[1:])
	return 0

print(find_combinations())