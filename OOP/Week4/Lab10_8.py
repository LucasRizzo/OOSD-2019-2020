def first_half(my_string):
    if len(my_string) % 2 == 1:
        print("Odd length")
        return my_string
    else:
        return(my_string[:len(my_string)//2])


print(first_half("Python"))
