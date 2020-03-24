def check_input(input):
    if input == "y" or input == "n" :
        return True
    return False


capitals = {}

while True :
    country_str = input ( "Please enter a country: " )
    capital_str = input ( "Please enter the country's capital: " )
    capitals[country_str] = capital_str
    loop = input ( "Do you want to enter another country? (y/n): " )
    while (check_input(loop) == False ):
        loop = input ( "Do you want to enter another country? (y/n): " )

    if loop == "n":
        break


value_key_list = []
for key, val in capitals.items():
    value_key_list.append((val, key))
value_key_list.sort()

for val, key in value_key_list:
    print (key, ": " , val)
