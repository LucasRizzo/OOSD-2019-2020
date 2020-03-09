list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
new_list = []

for el in list:
    if el not in new_list:
        new_list.append(el)

list = new_list
del new_list

print (list)

