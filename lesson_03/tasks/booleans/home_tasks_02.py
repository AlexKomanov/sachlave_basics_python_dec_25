# "5 5 5" -> ["5", "5", "5"]  <----- default behavior
a, b, c = map(int, input().split())

print(a == b and b == c and a == c)

print(a == b == c)