import string

# Exercise 15: Remove special symbols / punctuation from a string

print(string.punctuation)

# Given:
str1 = "/*Jon is @developer & musician"

# Using loop + conditions
# for letter in str1:
#     if letter in string.punctuation:
#         str1 = str1.replace(letter, "")

print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))
print("New string is: ", new_str)




# Expected Output:
# "Jon is developer musician"

