temp = input("Enter Temperature: ")
float_temp = float(temp[:-1])
char_in_temp = temp[-1]
if char_in_temp == "C":
    print(str(float_temp) +"C")
    print(str(round((9*float_temp)/5+32,2))+"F")
    print(str(round(float_temp+273,2))+"K")
elif char_in_temp == "F":
    
    print(str(round((float_temp-32)*5/9,2))+"C")
    print(str(float_temp) +"F")
    print(str(round((float_temp-32)*5/9+273,2))+"K")
elif char_in_temp == "K":
    print(str(round(float_temp-273,2)) +"C")
    print(str(round((float_temp-273)*9/5+32,2))+"F")
    print(str(float_temp)+"K")