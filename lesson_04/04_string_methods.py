# lower()
# text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# print("Alexander KoMANOV".lower())
# print(text.lower())
# print("AAA".lower() == "aaa".lower())

# upper()
# text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# print(text.upper())

# capitalize()
# text = "abcde abcde abcde"
# print(text.capitalize())

# title()
# text = "abcde abcde_abcde"
# print(text.title())
# print(id(text))
# print(id(text.title()))
# print(text)

# split()
# text = "abcde,abcde,abcde"
# text_2 = "abcde abcde abcde"
# print(text.split(","))
# print(text_2.split())
# print(type(text.split()))

# find()
# text = "Alexander"

# print("l" in text)
# print("z" in text)

# print(text.find("e"))
# print(text.find("X"))
# print(text.find("X") != -1)
# print(text.find("x") != -1)

# print(text.find("X"))
# print(text.upper().find("X"))
# print(text.find("a"))
# print(text.lower().find("a"))

# index()
# text = "Alexander"
#
# print(text.index("exand"))
# print(text.index("Alex"))
# print(text.index("X")) # ValueError: substring not found

# count()
# text = "Alexander"

# print(text.count("e"))
# print(text.count("X"))
# print(text.count("X") != 0)
# print(text.count("x") != 0)
# print(text.count('a'))
# print(text.lower().count('a'))

# replace()
# text = "Alexander,,,,,Komanov"
# print(text)
# print(text.replace("a", "b"))
# print(text.replace(",", ":"))
# print(text.replace(",", ":", 3))

# join()
# text = "hello"
# print(",".join(text))

students = "Ivanov Petrov Sidorov"
list_of_students = students.split(" ")
print(list_of_students)
string_with_students = ", ".join(list_of_students)
print(string_with_students)
print("Students are: " + string_with_students)