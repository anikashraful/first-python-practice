#finding sum of even numbers in a list


lst = [1, 2, 3, 4]

total = sum(x for x in lst if x % 2 == 0 )
print(total)