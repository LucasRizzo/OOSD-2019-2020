string = "abc"

new_string = ""
for char in string:
    new_string += chr(ord(char) + 1)

print(new_string)
