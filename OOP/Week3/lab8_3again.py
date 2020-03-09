string = "Hello there"

if len(string) < 4:
    print("Length is less than 4")
else:
    new_string = string[:2] + string[len(string) - 2 : len(string)]
    print(new_string)

