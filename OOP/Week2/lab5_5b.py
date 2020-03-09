is_summer = input("Is it summer? (Yes or No): ")
temp = int(input("What is the temperature: "))

if is_summer == "Yes":
    if 60 <= temp <= 100:
        print("We play!")
    else:
        print("We don't play!")
elif 60 <= temp <= 90:
    print("We play!")
else:
    print("We don't play!")
