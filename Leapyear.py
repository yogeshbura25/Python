year = int(input())
if year % 400 == 0:
    print("True")
if year % 4 == 0 and year % 100 != 0:
    print("True")
else:
    print("False")
    