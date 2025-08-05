#check the year is leap year or not


year = 2024

if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0):
	print('leap year!')
else:
	print('not leap year')