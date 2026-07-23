a,b,c=10,20,30
if a>b:
    if a>c:
        print("a is largest Number")
else:
    if b>c:
        print("b is largest number")
    else:
        print("C is largest number")


marks = int(input("Enter your marks:"))
if (0<= marks and marks>40):
    print("The grade is D")
elif (40<= marks and marks >60):
    print("The grade is C")
elif (60<= marks  and marks>80):
    print("The grade is B")
elif (80 <= marks and marks >=100):
    print("The grade is A")
