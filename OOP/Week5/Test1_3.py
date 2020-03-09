import string


def format_time(date_time):

    # Separate date and time by the space character
    # "21/02/2020 18:06:00"
    date, time = date_time.split()

    # Separate date by the / character. If the resulting number of elements is different than 3
    # then date does not have the right number of parameters
    if len(date.split("/")) != 3:
        print ("Date has not correct number of parameters")
        return

    # Separate time by the : character. If the resulting number of elements is different than 3
    # then time does not have the right number of parameters
    if len(time.split(":")) != 3:
        print ("Time has not correct number of parameters")
        return

    # Since we know we can split data, split it in three variables
    day, month, year = date.split("/")

    # Check whether days is between 1 and 31. Not checking leap years or if number of days match the month
    if not 1 <= int(day) <= 31:
        print("Days are wrong")
        return

    # Check whether month is between 1 and 12
    if not 1 <= int(month) <= 12:
        print("Months are wrong")
        return

    # Check whether year is between 0 and 9999. 9999 could be changed
    if not 0 <= int(year) <= 9999:
        print("Year is wrong. Only values between 0 and 9999 accepted")
        return

    # Since time was checked it can be split in three variables
    hour, min, sec = time.split(":")

    # Check whether hour is between 0 and 23
    if not 0 <= int(hour) <= 23:
        print("Hour is wrong")
        return

    # Check whether minutes is between 0 and 59
    if not 0 <= int(min) <= 59:
        print("Minutes are wrong.")
        return

    # Check whether seconds is between 0 and 59
    if not 0 <= int(sec) <= 59:
        print("seconds are wrong.")
        return

    # Print as required in the question
    line1 = "-> " + str(day) + "/" + str(month) + "/" + year
    line2 = "-> " + str(hour) + ":" + str(min) + ":" + sec
    line3 = "-> " + str(month) + "/" + year
    # Add am and change to pm if necessary
    line4 = "-> " + "a.m."
    if int(hour) > 11:
        line4 = "-> " + "p.m."

    print(line1)
    print(line2)
    print(line3)
    print(line4)


# Main code and tests
format_time("21/02/2020 18:06:00")
print()
format_time("37/05/1950 12:00:00")
print()
format_time("01/01/1900 25:06:00")

