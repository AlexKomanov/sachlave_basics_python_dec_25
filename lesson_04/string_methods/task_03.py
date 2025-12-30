input_string = input("Enter a word: ")

print(input_string[0:3].upper() + input_string[3:-3].lower() + input_string[-3:].upper())