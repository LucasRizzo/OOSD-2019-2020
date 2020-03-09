import random

count = 0
numerator = 0

while count < 10000000:
    x = random.randint(1, 100)
    if x <= 1:
        numerator += 1
    count += 1
    print ("Probability: ", numerator/count * 100, "%")




