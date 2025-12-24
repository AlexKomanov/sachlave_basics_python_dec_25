# a = int(input())
# b = int(input())
# c = int(input())

a, b, c = map(int, input("Enter 3 numbers: ").split())

print(f"(a+b*c) = {(a+b*c)}")
print(f"(a*b+c) = {(a*b+c)}")
print(f"(a*(b+c)) = {(a*(b+c))}")
print(f"(a*b*c) = {(a*b*c)}")
print(f"((a+b)*c) = {((a+b)*c)}")
print(f"(a+b+c) = {(a+b+c)}")
print("max = ", max((a+b*c), (a*b+c), (a*(b+c)), (a*b*c), ((a+b)*c), (a+b+c)))