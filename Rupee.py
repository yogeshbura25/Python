amount = int(input())
thousand = int(amount / 2000)
remaining = amount % 2000
five_hundred = int(remaining / 500)
remaining = remaining % 500
two_hundred = int(remaining / 200)
remaining = remaining % 200
fifty = int(remaining / 50)
remaining = remaining % 50
twenty = int(remaining / 20)
remaining = remaining % 20
five = int(remaining / 5)
remaining = remaining % 5
two = int(remaining / 2)
remaining = remaining % 2 
one = int(remaining / 1)
remaining = remaining % 1 
print("2000:" + str(thousand) + " 500:" + str(five_hundred) + " 200:" + str(two_hundred) + " 50:" + str(fifty) + " 20:" + str(twenty) + " 5:" + str(five) + " 2:" +str(two) + " 1:" + str(one))