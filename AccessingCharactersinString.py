#stringFunctions
s = " We are Coming for you, WE are ? who you are ? Why you are coming and What you want ? "

#type 
print(type(s))

#length of String
print(len(s))

#Slicing
r = (s[6:66])
print(r)
print(len(r))
print(s[2:])
print(s[:17])

#isDigit
r = s.isdigit()
print(r)

#strip removes 
r = s.strip(" ")
print(r) 
r = s.strip("W")
print(r)

#lower and upper CASE Letter's
print(s.lower())
print(s.upper())

#print's only upper Letter's
r = ""
for eachChar in s:
    if eachChar.isupper():
        r = r + eachChar
print(r)

#unicode
print(ord("y"))
print(ord("b"))

print(s[6:23:17])

#count 
r = s.count("you")
print(r)

#find
r = s.find("are")
print(r)

newString = "They are many string functions in python"
print(newString)