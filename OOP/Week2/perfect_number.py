number = int(input("Please enter an upper limit: "))

my_range = range(1, number)


for n in my_range:
    sum = 0

    for divisor in range(1, n):
        if n % divisor == 0:
            sum += divisor

    print ("N = ", n)
    if sum == n:
        print("Perfect number")
    elif sum < n:
        print("Deficient number")
    else:
        print("Abundant number")
