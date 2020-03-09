def sum_divisors(number):
    if number < 0:
        print ("Negative number. Only positive numbers accepted.")
        return
    sum = 0
    divisors = ""
    for i in range(1,number+1):
        if number % i == 0:
            sum += i
            # Add the divisor to the resulting string
            divisors += str(i)
            # If if it not the last number add + sign too look like an equation
            if i < number:
                divisors += " + "

    print(divisors, "=", sum)


# Main code
sum_divisors(20)
sum_divisors(33)
sum_divisors(42)
sum_divisors(-1)
