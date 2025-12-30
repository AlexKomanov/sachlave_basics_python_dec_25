#  -- LAB --
#  We're going to write a script that takes user input,
#  so that we're not working with static content, and print out some
#  information and permutations of the string that the user has entered.

message = input("Enter a message: ")

# Print first character from the User's Input
print("First character:", message[0])

# Print last character from the User's Input
print("Last character:", message[-1])

# Print middle character from the User's Input
print("Middle character:", message[int(len(message) / 2)])

# Print the Even Index Characters
print("Even index characters:", message[0::2])

# Print the Odd Index Characters
print("Odd index characters:", message[1::2])

# Print the String in Reverse
print("Reversed message:", message[::-1])