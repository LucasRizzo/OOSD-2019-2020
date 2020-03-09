number_str = input("Input a floating-point number: ")
while True:
    try:
        number_float = float(number_str)
    except ValueError:
        print("Please input a floating-point number")
        number_str = input("Input a floating-point number: ")
    else:
        break
print("Number is",number_float)
