def insert_string_middle(string1, string2):
    result = string1[:len(string1)//2] + string2 + string1[len(string1)//2:]
    return result

print(insert_string_middle("{{}}","PHP"))
