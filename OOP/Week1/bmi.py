weight_str = input("Please enter your weight in kg: ")
height_str = input("Please enter your height in meters: ")

weight_float = float(weight_str)
height_float = float(height_str)

bmi = weight_float / (height_float ** 2)

print("Your BMI is: ", round(bmi, 2))

if bmi < 18.5:
    print("You are underweight")
elif bmi < 24.9:
    print("Normal weight")
elif bmi < 29.9:
    print("You are overweight")
else:
    print("You are obese")
