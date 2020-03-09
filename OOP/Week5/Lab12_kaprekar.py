def is_kaprekar(number):
    power = str(number ** 2)

    if int(power[:len(power) // 2]) + int(power[len(power) // 2:]) == number:
        return True

    if int(power[:len(power) // 2 + 1]) + int(power[len(power) // 2 + 1:]) == number:
        return True

    return False

def print_kaprekars(upper_limit):
    kaprekars = ""
    for i in range(10,upper_limit + 1):
        if is_kaprekar(i):
            kaprekars += str(i) + " "
    print ("The list of kaprekars numbers from 10 to", upper_limit, "is: " )
    print(kaprekars)


upper_limit = int(input("Please enter an upper limit: "))
print_kaprekars(upper_limit)
