list_tuple = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

# only_numbers = []
# for el in list_tuple:
#     only_numbers.append(el[1])
#
# only_numbers.sort(reverse=True)
#
# result_list = []
# for el1 in only_numbers:
#     for el2 in list_tuple:
#         if el1 == el2[1]:
#             result_list.append(el2)
#             break
#
# list_tuple = result_list

# list_tuple.sort(key = lambda x: x[1], reverse=True)
list_tuple = sorted(list_tuple, key = lambda x: x[1], reverse=True)

print(list_tuple)



