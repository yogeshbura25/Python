secret_key = {"a" : "z", "b" : "y", "c": "x", "d" : "w","e" : "v","f" : "u","g":"t",
"h": "s","i" : "r","j": "q","k":"p","l" : "o","m" : "n","n" :"m","o" : "l",
"p" : "k","q":"j","r":"i","s":"h","t":"g","u":"f","v":"e","w":"d","x":"c","y":"b","z":"a"," " : " "}
message = input("Enter Message: ").lower()
space = ""
for char in message:
    if char in secret_key.keys():
        space += secret_key[char]
print(space)
