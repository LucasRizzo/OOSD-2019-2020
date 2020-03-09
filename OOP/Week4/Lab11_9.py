def common_member(list1, list2):
    for el1 in list1:
        if el1 in list2:
            return True

    return False


list1 = [1, 2, 3, 4, 5, 6]
list2 = [10, 9, 8, 7, 6]

print(common_member(list1, list2))
