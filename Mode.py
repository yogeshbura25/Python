a = list(map(int, input().split(",")))
count = 0 
mode = 0 
for i in a:
    x = a.count(i)
    if x > count:
        count = x 
        mode = i 
print(mode)