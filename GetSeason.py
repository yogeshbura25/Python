month = int(input())
January = 1
February = 2
March = 3
April = 4
May = 5
June = 6
July = 7
August = 8 
September = 9
October = 10 
November = 11
December = 12
if month in [January,December,November]:  
    print("Winter") 
elif month in [February, March]:
    print("Spring")
elif month in [April,May,June]:
    print("Summer")
elif month in [July, August]:
    print("Rainy")
else:
    print("Autumn")