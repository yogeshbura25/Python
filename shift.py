string  = input()
empty_space = ""
another_empty_space = ""
for each_char in string:
    if each_char.isdigit():
        empty_space += each_char
    else:
        another_empty_space += each_char
print(another_empty_space + empty_space)