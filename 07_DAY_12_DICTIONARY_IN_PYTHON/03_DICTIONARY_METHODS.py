student = {
    "Name": "Aman Kumar",
    "Reg. No.": 23157128040,
    "Semester": "3rd-Sem",
    "Branch": "CSE(AI&ML)",
    "Score":{
        "OOPs": 19,
        "DSA": 14,
        "AEC": 18,
        "M-III": 16.5,
        "TW": 14.5
    }
}
print(student.keys())
print(student.values())
print(student.items())
print(list(student.keys()))
print(tuple(student.keys()))
print(student["Score"])
print(student.get("Aman"))
