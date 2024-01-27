#Even numbers

n = int(input("Enter a Number: "))

for even  in range(1, n + 1):
    if even % 2 == 0:
        print(even)
        
