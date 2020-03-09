def difference(list1, list2):
    list_difference = []
    for el in list1:
        if el not in list2:
            list_difference.append(el)

    return list_difference

list1 = [1, 2, 3, 4, 5, 6]
list2 = [10, 9, 8, 7, 6]

print(difference(list2, list1))


