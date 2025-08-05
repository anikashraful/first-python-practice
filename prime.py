#checking if a number is prime or not

num = 7
is_prime = True

for i in range(2, num):
	if num % i == 0:
		is_prime = False
		break
if is_prime and num > 1:
	print('prime')
else:
	print('not prime')