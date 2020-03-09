# (a)
#my_int = int(input("Please enter an integer: "))

#sum = 0
#for i in range(1, my_int + 1):
#    sum += i

#print (sum)

# (b)
#my_int = int(input("Please enter an integer: "))

#for i in range(1, my_int + 1):

#    sum = 0
#    for j in range(1, i + 1):
#        sum += j
#        if (j < i):
#            print(j, " + ", end = "")
#        else:
#            print(j, " = ", end = "")

#    print (sum)

# (c)
my_int = int(input("Please enter an integer: "))

for i in range(2, my_int + 1, 2):
    sum = 0
    count = 1
    result = ""
    for j in range(1, i + 1):
        sum += j
        count += 1
        if j < i:
            result += str(j) + " + "
        else:
            result += str(j) + " = "

    if sum % count == 0:
        print (result, sum)
