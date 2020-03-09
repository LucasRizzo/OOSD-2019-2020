import string


# function to check if all elements are present or not
def check(s):
    return set(string.ascii_lowercase) - set(s.lower()) == set([])


# driver code
sentence = "The quick brown fox jumps over the lazy dog"
if check(sentence):
    print("The string is a pangram")
else:
    print("The string isn't a pangram")
