#finding sum of odd numbers ina list

lst = [1, 2, 3, 4, 5, 6, 7]


total = sum(x for x in lst if x % 2 != 0)
print(total)