string = input()
if string.isdigit():
    print("Digit")
elif string != string.upper():
    print("Lowercase Letter")
elif string != string.lower():
    print("Uppercase Letter")
else:
    print("Special Character")
    