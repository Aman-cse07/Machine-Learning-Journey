marks = int(input("Enter your marks: "))

if 0 <= marks <= 40:
    print("The grade is D")
elif 40 < marks <= 60:
    print("The grade is C")
elif 60 < marks <= 80:
    print("The grade is B")
elif 80 < marks <= 100:
    print("The grade is A")
else:
    print("Invalid marks")
