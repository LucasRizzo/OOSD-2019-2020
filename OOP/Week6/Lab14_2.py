def safe_input(prompt, prompt_type):

    if type(prompt) == prompt_type:
        return prompt

    while True:
        try:
            converted = prompt_type(prompt)
        except ValueError:
            print(prompt, "cannot be converted to", prompt_type)
            prompt = input("Please input a new prompt: ")
        else:
            return converted


# Main code
safe_input(input("Please enter a number: "), int)
safe_input(input("Please enter a float: "), float)
safe_input(input("Please ener a string: "), str)
