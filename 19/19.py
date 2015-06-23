
START = 1901
END = 2001

def is_leap_year(year):
	if year % 100 == 0:
		return year % 400 == 0
	else:
		return year % 4 == 0

def number_of_days_per_month(month, leap_year):
	if month == 2:
		return 28 if not leap_year else 29
	if month in [4, 6, 9, 11]:
		return 30
	return 31

sundays = 0
total_days = 0
for year in range(START, END):
	for month in range(1, 13):
		if total_days % 7 == 0:
			sundays += 1
		total_days += number_of_days_per_month(month, is_leap_year(year))

print(sundays)