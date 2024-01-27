#List 

r = -5
d = 9.5
list_data = [18, "TwentyFive", r, "Python", 45, d, True]

#type
print(type(list_data))     #<class 'list'>

#length
print(len(list_data))      #7

#accessing an element in list
print(list_data[3])        #Python
print(list_data[2])        #-5

#Concatenation with another list
new_list = ["numberFour",389668,"@",-5756]
result = list_data + new_list
print(result)              #[18, 'TwentyFive', -5, 'Python', 45, 9.5, True, 'numberFour', 389668, '@', -5756]

#iterating over a list
for eachChar in (list_data):    #18
    print(eachChar)             #TwentyFive
                                #-5
                                #Python
                                #45
                                #9.5
                                #True
    
    
#list repetition
print(list_data * 3)          #[18, 'TwentyFive', -5, 'Python', 45, 9.5, True, 18, 'TwentyFive', -5, 'Python', 45, 9.5, True, 18, 'TwentyFive', -5, 'Python', 45, 9.5, True]   
print(new_list * 4)           #['numberFour', 389668, '@', -5756, 'numberFour', 389668, '@', -5756, 'numberFour', 389668, '@', -5756, 'numberFour', 389668, '@', -5756]

#slicing
print(list_data[:2])
print(new_list[2:])
print(new_list[2:4])

#converting into list
color = "BalckYellow"
converted_list = (list(color))
print(len(converted_list))
combination = (list_data + new_list)
print(combination)

#modifying list change the value in list
list_data[3] = 25
print(list_data)

#unidque identifier
print(id(list_data))
print(id(new_list))
print(id(color))

#JoinigList
string_list = ['python is ',' progr','mming l','ngu','ge']
new_string = "a".join(string_list)
print(new_string)

#slicing
print(new_string[2:5])
