import random
s = input("Enter a string: ")

i = random.randint(0,len(s)-1)
j = random.randint(0,len(s)-1)

#if the i>=j re-generate the random numbers, otherwise the slicing won't work
while (i>=j):
    i = random.randint(0, len(s) - 1)
    j = random.randint(0, len(s) - 1)

new_string = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
print("Result: ", new_string)
print("Characters swapped: ", s[i], s[j])
