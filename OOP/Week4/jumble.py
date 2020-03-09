import random


# swap letters at index i and j
# assume i<j, otherwise don't swap and print error message
def swap_two_letters(string, i, j):
    if (i >= j):
        print("Problem with the index of letters to swap. Not swapped")
        return string

    return string[:i] + string[j] + string[i + 1:j] + string[i] + string[j + 1:]


def jumble_word_once(string):
    length = len(string)

    if length <= 3:
        print("Word too short to jumble")
        return string

    i = random.randint(1, length - 2)
    j = random.randint(1, length - 2)

    while i >= j:
        i = random.randint(1, length - 2)
        j = random.randint(1, length - 2)

    s1 = swap_two_letters(string, i, j)
    return s1


def jumble_word(string):
    for i in range(0, 3):
        string = jumble_word_once(string)

    return string


# main program
s1 = "abracadabra"
s1 = jumble_word(s1)
print(s1)



