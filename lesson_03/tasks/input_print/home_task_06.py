full_number = int(input("Enter a number: "))
# print(round(full_number / 1000)) # Can trigger a bug due to round function
print(full_number // 1000)