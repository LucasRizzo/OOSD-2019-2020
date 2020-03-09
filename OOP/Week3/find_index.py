river = "Mississippi"
target = input("Input a target to find: ")

for index in range(len(river)):
    if river[index] == target:
        print("Letter found at index", index)
        break
else:
    print("Letter", target, "not found in river", river)
