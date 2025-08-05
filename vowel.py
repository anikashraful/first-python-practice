#count vowels in a string

text = 'hello'

vowels = 'aeiou'

count = sum(1 for char in text.lower() if char in vowels)
print(count)

text1 = 'ashrafulalamanik'

count1 = sum(1 for char in text1.lower() if char in vowels)
print(count1)