# Get the first word
word = input("Please enter a word: ")

# Repeat until user enters a dot
while word != ".":
    new_word = ""
    # If word starts with a vowel just add yay to the end
    if word[0] in "aeiou":
        new_word = word + "yay"
    # If word does not start with a vowel
    else:
        # Get the consonants at the beginning
        consonants = ""
        index = 0
        # Keep iterating until finds a vowel
        while index < len(word) and word[index] not in "aeiou":
            consonants += word[index]
            index += 1

        # New word is formed by letter after consonants + consonants at the beginning + ay
        new_word = word[index:] + consonants + "ay"

    print ("New word is: ", new_word)
    word = input("Please enter another or . to end: ")

