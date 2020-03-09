my_dict = { "1" : "one" , "2" : "two" , "3" : "three" , "4" : "four" , "5" : "five" , "6" : "six" , "7" : "seven" , "8" : "eight" , "9" : "nine" , "0" : "zero" }
n_str = input ( "Enter an integer: " )
my_keys = my_dict.keys()
for char in n_str:
    if char in my_keys:
        print (my_dict[char], end = " " )
    else :
        print ( "Input error. Only numbers accepted." )
