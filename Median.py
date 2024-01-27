s = list(map(int,input().split(",")))
s = sorted(s)
if len(s) % 2 == 0:
    median = s[(len(s) // 2) - 1] + s[(len(s) // 2)]
    print(median / 2)
else:
    median = s[len(s) // 2]
    print(median)