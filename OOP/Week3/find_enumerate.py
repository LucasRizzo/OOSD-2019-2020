river = "Mississippi"
target = input("Input a target to find: ")

for index,letter in enumerate(river):
    if letter == target:
        print("Letter found at index", index)
        break
else:
    print("Letter", target, "not found in river", river)



