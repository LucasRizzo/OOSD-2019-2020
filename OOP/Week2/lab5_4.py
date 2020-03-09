a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
c = int(input("Please enter the third number: "))

if a > b:
    if a > c:
        print("Largest is ", a)
    else:
        print("Largest is ", c)
else:
    if b > c:
        print("Largest is ", b)
    else:
        print("Largest is ", c)
