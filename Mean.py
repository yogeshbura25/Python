num = list(map(int,input().split(",")))
lens_nums = len(num)
sum = 0 
for i in num:
    sum += i 
mean = sum / lens_nums 
print(mean)