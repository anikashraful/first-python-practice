#check if a string is a palindrome


text = 'racecar'

if text == text[::-1]:
	print('palindrome')
else:
	print('not palindrome')