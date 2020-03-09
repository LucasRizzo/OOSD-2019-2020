# get input
number_str = input("Please enter a number to check:")
number = int(number_str)

# calculate the sum of the divisors
divisor = 1
sum_of_divisors = 0
while divisor < number:
    print("Testing ", divisor)
    if number % divisor == 0:  # divisor evenly divides the number
        sum_of_divisors = sum_of_divisors + divisor
        print(divisor, " is a divisor of ", number, ". New sum is ", sum_of_divisors)
    else:
        print(divisor, " is a not divisor of ", number)

    divisor = divisor + 1

# classify the result
if number == sum_of_divisors :
    print(number, " is perfect")
else:
    print(number, " is not perfect")



