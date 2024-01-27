m = int(input("Enter Input"))
p = int(input("Enter Input"))
c = int(input("Enter Input"))
a = m >= 70 and p >= 60 and c >= 60
d = m + p + c >= 180
print(a or d)