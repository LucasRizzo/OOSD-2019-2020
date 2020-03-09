is_weekend = input("Is it weekend? (Yes or No): ")
cigars = int(input("How many cigars do you have: "))

if is_weekend == "Yes":
    if cigars >= 40:
        print("Party successful")
elif 40 <= cigars <= 60:
    print("Party successful")
else:
    print("Party unsuccessful")
