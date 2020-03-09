

sum = 0
while True:
    number_str = input("Please enter a number: ")

    if number_str == ".":
        print ("Final sum is: ", sum)
        break

    number = int(number_str)

    if (number % 2 == 0):
        sum += number
    elif (number % 2 == 1):
        print ("Number is not even! Enter even numbers only.")



