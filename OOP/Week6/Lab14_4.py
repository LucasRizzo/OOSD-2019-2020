number1 = input("Please enter first number: ")
number2 = input("Please enter second number: ")
number3 = input("Please enter third number: ")

try:
    number1 = float(number1)
    number2 = float(number2)
    number3 = float(number3)

    result = (number1 / number2) + number3
    print(result)
except ValueError:
    print("No correct values were passed.")
except ZeroDivisionError:
    print("Second number cannot be 0")

