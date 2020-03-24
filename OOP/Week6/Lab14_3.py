def prompt_open(mode):
    file_str = input("Enter file name: ")

    while True:
        try:
            file = open(file_str, mode)
        except IOError:
            file_str = input("File could not be opened. Please enter a valid file name: ")
        else:
            return file


file1 = prompt_open("r")
