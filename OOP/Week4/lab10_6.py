def first_and_last_two(my_string):

    if (len(my_string) < 4):
        print("Length is less than 4")
        return my_string
    else:
        result = my_string[:2] + my_string[-2:]
        print (result)


# Main code
my_string = input("Enter a message: ")
first_and_last_two(my_string)
