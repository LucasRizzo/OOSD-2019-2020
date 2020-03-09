# Asks for score ahead
score_ahead_str = input("How many points ahead? ")
score_ahead_int = int(score_ahead_str)

# Subtract 3 from the score ahead
score_ahead_int -= 3

team_ahead_has_the_ball = input("Does the team ahead has the ball? (Yes or No) ")

if team_ahead_has_the_ball != "No" and team_ahead_has_the_ball != "Yes":
    print("Wrong input!")

if team_ahead_has_the_ball == "Yes":
    score_ahead_int += 0.5

if team_ahead_has_the_ball == "No":
    score_ahead_int -= 0.5

if score_ahead_int < 0:
    score_ahead_int = 0

score_ahead_int = score_ahead_int ** 2

seconds_left = int(input("How many seconds left?"))

if score_ahead_int > seconds_left:
    print("Lead is safe")
else:
    print("Lead is not safe")




