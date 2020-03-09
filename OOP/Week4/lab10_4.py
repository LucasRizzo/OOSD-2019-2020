def sum_of_numbers():
    number = int(input("Please enter a number: "))
    sum = 0
    for i in range(1, number + 1):
        sum += i
    return sum


# Main code
print(sum_of_numbers())
