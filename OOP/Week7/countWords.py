import string


def add_word(word, word_count_dict):
    """Update the word frequency: word is the key, frequency is the value"""
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1


def process_line(line, word_count_dict):
    """Process the line to get lowercase words to add to the dictionary"""
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        word = word.lower().strip()
        # get comas, periods, and other punctuation as well
        word = word.strip(string.punctuation)
        add_word(word, word_count_dict)


def pretty_print(word_count_dict):
    """Print nicely from highest to lower frequency"""
    # create a list of tuples, (value, key)
    # value_key_list = [(value, key) for key, value in d.items()]
    value_key_list = []
    for key, value in word_count_dict.items():
        value_key_list.append((value, key))
    # sort method sorts on list's first element, the frequency.
    # reverse to get the biggest first
    value_key_list.sort(reverse=True)

    my_dict = {}
    my_dict = sorted([(v,k) for k, v in my_dict.items()], reverse = True)

    print("{:11s}{:11s}".format("Word", "Count"))
    print("_" * 21)
    for val, key in value_key_list:
        print("{:12s} {:<3d}".format(key, val))


def main():
    word_count_dict = {}
    file = open("hare_and_tortoise.txt")
    for line in file:
        process_line(line, word_count_dict)
    print("Length of the dictionary:", len(word_count_dict))
    pretty_print(word_count_dict)


main()
