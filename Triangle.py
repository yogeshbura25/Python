a = int(input("Enter Side: "))
b = int(input("Enter Side: "))
c = int(input("Enter Side: "))
e = (a == b == c)
i = (a  == b or a == c or b == c)
s = (a != b != c)
if e:
    print("Equilateral")
elif i:
    print("Isosceles")
elif s:
    print("Scalene")
    