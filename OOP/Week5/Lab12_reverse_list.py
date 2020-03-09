def reverse_second_words(text):
    text_list = text.split()
    for index, word in enumerate(text_list):
        if index % 2 == 1:
            text_list[index] = word[::-1]

    return " ".join([word for word in text_list])


text = "I love you for a lifetime"
print(reverse_second_words(text))
