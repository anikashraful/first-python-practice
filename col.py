#Check if a String Contains Only Letters

text = 'python'

if text.isalpha():
	print('only letters')
else:
	print('not')



#Find Sum of Digits

num = 123

total = sum(int(d) for d in str(num))
print(total)