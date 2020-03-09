# get input
number_str = input("Please enter a decimal number to convert:")
number = int(number_str)

binary = ""


# number = 12 // 2 = 6 // 2 = 3 // 2 = 1
# binary = "0011"
# remainder = 0, 0, 1, 1

while number // 2 > 0:
    remainder = number % 2
    binary = binary + str(remainder)
    number = number // 2

remainder = number % 2
binary = binary + str(remainder)

binary = binary[::-1]

print (binary)
