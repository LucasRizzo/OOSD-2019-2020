import string

original_str = input("Input a string: ")
modified_str = original_str.lower()

bad_chars = string.whitespace + string.punctuation

print(bad_chars)

for char in modified_str:
    if char in bad_chars:
        modified_str = modified_str.replace(char,"")

if modified_str == modified_str[::-1]:
    print("The original string is:", original_str, "\n\
           The modified string is:", modified_str, "\n\
           The reversal is:", modified_str[::-1], "\n\
           String is a palindrome.")
else:
    print("The original string is:", original_str, "\n\
           The modified string is:", modified_str, "\n\
           The reversal is:", modified_str[::-1], "\n\
           String is not palindrome.")
