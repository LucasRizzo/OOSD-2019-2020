import random
random_number = random.randint(0, 100)

guess = int(input("Please guess a number from 0 to 100: "))

while (0 <= guess <= 100):
    if guess == random_number:
        print ("You win!")
        break
    if guess > random_number:
        print("Guess is too high")
    else:
        print("Guess is too low")

    guess = int(input("Please guess another number from 0 to 100: "))
else:
    print("You left.")

