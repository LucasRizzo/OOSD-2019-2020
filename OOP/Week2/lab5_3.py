first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

operator = input("Enter the operator: ")

result = 0

if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "/":
    result = first_number / second_number
elif operator == "*":
    result = first_number * second_number
else:
    print ("Operator not recognized")

print(first_number, " ", operator, " ", second_number, " = ", result)
