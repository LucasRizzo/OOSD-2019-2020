def factorial(number):
    result = 1
    string_result = ""
    for i in range(1, number+1):
        result *= i
        if i < number:
            string_result += str(i) + " * "
        else:
            string_result += str(i) + " = "

    print(string_result, result)


# Main function
number = int(input("Please enter a number: "))
factorial(number)
