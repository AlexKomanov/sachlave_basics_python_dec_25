sentence = "hello world of python"
print(sentence[0])
print(sentence[-1])
# print(sentence[50]) # IndexError: string index out of range
print(sentence[0:4+1])
print(sentence[0:12:2])
print(sentence[::-1]) # reverse string without using a function
print(sentence[-1:-6:-1])
print(sentence[-10:-1:])
print(sentence[::])
print(sentence[0:])
print(sentence[0:50])

text_len = len(sentence)
print(sentence[0:text_len])
print(sentence[0:text_len-1])

print(id(sentence))
sentence = sentence[0] + sentence[1:]
print(sentence)
print(id(sentence))
# sentence[1] = "" # TypeError: 'str' object does not support item assignment

