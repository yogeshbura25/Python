#Tuples  

y = "SIX"
tuple_a = (18, "TwentyFive", y, 45, 78.5, True)    
print(tuple_a)     #(18, 'TwentyFive', 'SIX', 45, 78.5, True)

#LengthOfElement
print(len(tuple_a))     #6

#AccessingTupleElements
print(tuple_a[0])     #18
print(tuple_a[1])     #TwentyFive
print(tuple_a[2])     #SIX
print(tuple_a[3])     #45
print(tuple_a[4])     #78.5
print(tuple_a[5])     #True

#TupleSlicing
print(tuple_a[0:6])     #(18, 'TwentyFive', 'SIX', 45, 78.5, True)
print(tuple_a[0:3])     #18, 'TwentyFive', 'SIX')
print(tuple_a[0:])      #(18, 'TwentyFive', 'SIX', 45, 78.5, True)
print(tuple_a[:6])      #(18, 'TwentyFive', 'SIX', 45, 78.5, True)
print(tuple_a[0:4:6])   #(18,)
print(tuple_a[-1:-4:-2])#(True, 45)

#MemberShipCheckInTuple
is_part = "SIX" in tuple_a     #True
print(is_part)

is_part = 25 in tuple_a        #False
print(is_part)

#iteratingoveralist           #18
for eachChar in tuple_a:      #TwentyFive  
    print(eachChar)           #SIX
                              #45 
                              #78.5
                              #True 
                            
#TupleRepetition
print(tuple_a * 3)     #(18, 'TwentyFive', 'SIX', 45, 78.5, True, 18, 'TwentyFive', 'SIX', 45, 78.5, True, 18, 'TwentyFive', 'SIX', 45, 78.5, True)

#ConvertingintoTuple
color = "BLACKYELLOWWHITEGREY"
result = tuple(color)
print(result)         #('B', 'L', 'A', 'C', 'K', 'Y', 'E', 'L', 'L', 'O', 'W', 'W', 'H', 'I', 'T', 'E', 'G', 'R', 'E', 'Y')
print(type(result))   #<class 'tuple'>
print(len(result))    #20