NUMBER_TO_LETTERS_TEXT = """
1 one
2 two
3 three
4 four
5 five
6 six
7 seven
8 eight
9 nine
10 ten
11 eleven
12 twelve
13 thirteen
15 fifteen
18 eighteen
20 twenty
30 thirty
40 forty
50 fifty
80 eighty
"""

NUMBERS_MAP = {int(k): v for k, v in [pair.split() for pair in NUMBER_TO_LETTERS_TEXT[1:-1].split('\n')]}

def number_to_letters(number):
    if number == 0:
        return ''
    if number in NUMBERS_MAP:
        return NUMBERS_MAP[number]
    elif number < 20:
        return NUMBERS_MAP[number - 10] + 'teen'
    elif number < 100:
        last_digit = int(str(number)[-1])
        if number - last_digit in NUMBERS_MAP:
            rest = NUMBERS_MAP[number - last_digit]
        else:
            first_digit = int(str(number)[0])
            rest = NUMBERS_MAP[first_digit] + 'ty'
        return rest + number_to_letters(last_digit)
    elif number < 1000:
        first_digit, rest = int(str(number)[0]), int(str(number)[1:])
        result = number_to_letters(first_digit) + 'hundred'
        if rest > 0:
            result += 'and' + number_to_letters(rest)
        return result
    elif number == 1000:
        # a thousand
        return 'onethousand'

result = 0
for number in range(1, 1001):
    word = number_to_letters(number)
    print(word)
    result += len(word)

print(result)

