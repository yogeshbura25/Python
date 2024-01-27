odd= int(input())
total = 0 
for each_Char in range(1, odd + 1):
    if each_Char % 2 == 1:
        total += each_Char
print(total)