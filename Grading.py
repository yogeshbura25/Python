External_Marks = int(input("Enter External Marks: "))
Internal_Marks = int(input("Enter Internal Marks: "))
Total_marks = External_Marks + Internal_Marks
print(Total_marks)

if Total_marks >= 75:
    print("Grade: A")
elif Total_marks >= 65:
    print("Grade: B")
elif Total_marks >= 55:
    print("Grade: C")
elif Total_marks >= 45:
    print("Grade: D")
elif Total_marks >= 35:
    print("Grade: E")
else:
    print("Grade: F")

    