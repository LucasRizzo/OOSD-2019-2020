def count_even_list(list):
    even_list = []
    for el in list:
        if el % 2 == 0:
            even_list.append(el)
    return even_list

print(count_even_list([1, 2, 3, 4, 5, 6]))

