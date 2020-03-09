def largest_list(list):
    largest = list[0]
    for el in list:
        if el > largest:
            largest = el
    return largest

print(largest_list([1, 2, 3, 4, 5, 6]))

