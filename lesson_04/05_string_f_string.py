name = "Alexander"
surname = "komanov"
age = 36

# print("Hello " + name + " " + surname + "! My age is: " + str(age))

# formatted_string = "Hello {2} {0}! My age is: {1}".format( surname, age, name)
# print(formatted_string)

# formatted_string = f"Hello {name.upper()} {surname.capitalize()}! My age next year will be: {age + 1}"
# print(formatted_string)

# x = 5
# y = 10
# result = x + y
#
# print(f"{x = }, {y = }, {result = }")

total = 100000000000
print(f"{total:,}")

pi = 3.1443435435
print(f"{pi:.2f}")

print(f"{name:*^21}")
print(f"{surname:*^21}")

BASE_URL = "https://www.reqres.in"
CASES_API = f"{BASE_URL}/cases"
USERS_API = f"{BASE_URL}/users"
USER_API = f"{USERS_API}/{name}"
print(f"{USER_API = }")