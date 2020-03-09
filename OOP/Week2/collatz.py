number = int(input("Please enter a number: "))

while number != 1:
    if number % 2 == 1:
        number = number * 3 + 1
    else:
        number /= 2

    print (number, end = " ")

