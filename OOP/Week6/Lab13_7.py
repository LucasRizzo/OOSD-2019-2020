# (a)
results = [n**2 for n in range(10)]
#print(results)

# (b)
colors = ['Red', 'Blue', 'Green', 'Black', 'White']
results = [c.upper() for c in colors]
# print(results)

# (c)
results = [num for num in range(1000) if num % 7 == 0]
# print(results)

# (d) #
#results = [num for num in range(1000) if '3' in list(str(num))]
results = [num for num in range(1000) if '3' in str(num)]
#results = [num for num in range(1000) for el in (str(num)) if el == "3"]
#print(results)

# (d)
teststring = 'Find all of the spaces in a string'
# print teststring.count(' ')   # normally I'd just do this, but for the practice....
results = [character for character in teststring if character == ' ']
#print(len(results))

# (e)
teststring = 'Find all of the letters in a string that are not vowels'
vowels = ['a', 'e', 'i', 'o', 'u']
results = [letter for letter in teststring if letter.lower() not in vowels]
#print(results)

# (f)
teststring = 'Find all of the words in a string that are less than 4 letters'
results = [word for word in teststring.split() if len(word) < 4]
# print(results)

# (g)
results = [number for number in range(1, 1001) if True in [True for divisor in range(2, 10) if number % divisor == 0]]
# print(results)
