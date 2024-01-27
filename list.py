names = ["Priya", "Raj", "Aishwarya", "Sanjay", "Neha", "Arjun", "Meera", "Rohan", "Anjali", "Karthik", "Deepa", "Ravi", "Pooja", "Vikram", "Sunita", "Manoj", "Smita", "Harish", "Reena", "Anil"]
ages = [25, 32, 28, 36, 22, 19, 30, 40, 27, 33, 21, 44, 29, 35, 24, 31, 26, 39, 42, 23]
genders = ["Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male"]
salaries = [220000.0, 210000.0, 195000.0, 230000.0, 205000.0, 198000.0, 225000.0, 203000.0, 198000.0, 215000.0, 192000.0, 235000.0, 199000.0, 205000.0, 212000.0, 200000.0, 198000.0, 225000.0, 215000.0, 190000.0, 220000.0]
for names, ages, genders, salaries in list(zip(names, ages, genders, salaries)):
     print(f"{names} : {ages} : {genders} : {salaries}")
