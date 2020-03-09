input_file = open("input.txt", "r")
output_file = open("output.txt", "w")

for line_str in input_file:
    new_str = ""
    line_str = line_str.strip() # Remove spaces from the beginning and end of the string
    for char in line_str:
        new_str = char + new_str # Concat at the left (reverse)
    print(new_str, file=output_file) # Print to output file
    # Include a print in the shell so we can observe the progress
    print("Line: {:12s} reversed is {:s}".format(line_str, new_str))

input_file.close()
output_file.close()



