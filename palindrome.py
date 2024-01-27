input_string = input()
palindrome_string = input_string[::-1]

if input_string == palindrome_string:
    print(input_string, "is Palindrome")
else:
    print("Not a Palindrome")
