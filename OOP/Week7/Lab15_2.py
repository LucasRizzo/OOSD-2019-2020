dict = {'a':15, 'c':35, 'b':20}

# print all the keys
# for key in dict.keys():
#     print(key)
#
# # print all the values
# for value in dict.values():
#     print(value)
#
# # print all the keys and value pairs
# for key, value in dict.items():
#     print (key, value)

# print all the keys and values in order of key
print(sorted([(k,v) for k,v in list(dict.items())]))

# to print all the keys and values pairs in order of value
print(sorted([(v,k) for k,v in list(dict.items())]))

