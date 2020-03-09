# Iterate over all 3 digit numbers (from 0 to 999)

contacts = {'bill': '353-1234', 'rich': '269-1234', 'jane': '352-1234'}
contacts["bill"] = "555-1234"

def search_phone(contacts):
    for key, value in contacts.items():
        if "555" in value:
            print (key, ": ", value)

search_phone(contacts)
