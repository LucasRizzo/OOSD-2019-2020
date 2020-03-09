string = "Monty Python"

new_string = ""
index = 0
for char in string:
    new_string += chr(ord(char) + index)
    index += 1

print(new_string)
