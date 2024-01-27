#Odd Number

n = int(input("Enter a Number: "))

for odd in range(1, n + 1):
    if odd % 2 == 1:
        print(odd)