marks = {
    "Aman":98,
    "Kumar":87,
    "Kunal":88,
    "Piyush":87,
    "Aiyush":85,
    "List":[1, 2, 3, 4, 5]
}

print(marks, type(marks))
print(marks["Aman"])
print(marks["List"])
n = input("Enter name:-") #For users if key match then return value from dictionary otherwise return "None".
print("Marks of entered name is:- ", marks.get(n))
