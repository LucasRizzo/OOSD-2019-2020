def odd_and_even_numbers(number):
    for i in range(number + 1):
        if i % 2 == 0:
            print(i, "is even")
        else:
            print(i, "is odd")


# Main code
n = int(input("Please enter a number: "))
odd_and_even_numbers(n)
