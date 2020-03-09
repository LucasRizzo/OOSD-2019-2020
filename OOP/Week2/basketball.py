points_ahead_int = [n for n in range(1,100000)]
seconds_remaining = [n for n in range(1,1000000)]
has_the_ball = ["Yes", "No"]

iterations = 0
for points in points_ahead_int:
    for seconds in seconds_remaining:
        for ball in has_the_ball:
            iterations += 1
            lead_calculation_float = float(points - 3)
            if ball == "Yes":
                lead_calculation_float += 0.5
            else:
                lead_calculation_float -= 0.5

            if lead_calculation_float < 0:
                lead_calculation_float = 0

            lead_calculation_float = lead_calculation_float ** 2

            if lead_calculation_float == seconds:
                print("I don't know")

print(iterations)
