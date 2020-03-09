
while True:
    is_birthday = input("Is it your birthday? (Yes or No): ")
    speed = int(input("What is the speed: "))

    bonus = 0
    if is_birthday:
        bonus = 5

    if speed <= 60 + bonus:
        print("No ticket")

    elif 61 + bonus <= speed <= 80 + bonus:
        print("Small ticket")

    elif speed + bonus >= 81:
        print("big ticket")

    if input("Do you want to try again? (Yes or No) ") == "No":
        break
