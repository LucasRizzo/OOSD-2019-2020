def replace_all(the_string, to_be_replaced, replace_with):
    the_string_list = the_string.split()

    for index, word in enumerate(the_string_list):
        if word in to_be_replaced:
            the_string_list[index] = replace_with[to_be_replaced.index(word)]

    return " ".join([word for word in the_string_list])


print(replace_all("This is a wonderful morning", ["is"], ["was"]))
print(replace_all("This is a wonderful morning", ["is", "morning"], ["was", "evening"]))
print(replace_all("John and Bill went to the shop", ["John", "Bill", "shop"], ["Mary", "Ann", "cinema"]))
