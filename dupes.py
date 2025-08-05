#check if a list contains dupes


lst = [1, 2, 2, 3]

if len(lst) != len(set(lst)):
	print('has dupes')
else:
	print('none')