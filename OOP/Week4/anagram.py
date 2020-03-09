def anagram(text):
    """return true if the two words are anagram and false otherwise"""

    #[return, true, if, the, two, words, are, anagram, and, false, otherwise, fi]
    words = text.split()

    for i in range(len(words)):
        for j in range(len(words)):
            word1 = words[i]
            word2 = words[j]
            # Sort the characters of the words
            word1_sorted = sorted(word1) # Sorted returns a sorted list
            word2_sorted = sorted(word2)

            # If the sorted words are identical return true (they are anagrams)
            if word1_sorted == word2_sorted:
                print (word1, " and ", word2, "are anagrams")
# Main code
anagram("return true if the two words are anagram and false otherwise fi")
