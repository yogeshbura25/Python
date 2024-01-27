units=int(input("Enter number of Units: "))
bill=0
if units <50:
    bill = 2 *units
elif units < 150:
    bill =(2 * 50) + (3 *(units-50))
elif units < 250:
    bill = (2 * 50) + (3 *100) + (5 * (units-150))
elif units >= 250:
    bill = (2 * 50) + (3 * 100) + (5 *100) + (8 *(units-250))
surcharge =(0.2 * bill)    
totalbill = (bill + surcharge)
print(totalbill)