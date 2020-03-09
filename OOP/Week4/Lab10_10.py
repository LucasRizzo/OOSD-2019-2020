def remove_substring(my_string, index1, index2):
    if index2 < index1:
        print (index1, "is greater than ", index2)
        return (my_string)

    result = my_string[:index1] + my_string[index2 + 1:]
    return result


sentence = input("Input a sentence: ")
index1 = int(input("Input the first index lesser than " + str(len(sentence)) + ": "))
index2 = int(input("Input the first index lesser than " + str(len(sentence)) + \
                   " and greater than " + str(index1) + ": "))

print(remove_substring(sentence, index1, index2))
