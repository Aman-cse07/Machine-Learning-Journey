marks = {
    "Name":"Aman Kumar",
    "Aman":98,
    "Kumar":87,
    "Kunal":88,
    "Piyush":87,
    "Aiyush":85,
    1 : "Sinha"
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Aman":100, "name":"Saumya Singh" , "name_1":"Shivangi Rathore"})
print(marks["Aman"])
print(marks)
print(marks.get("sahil")) #This return none value.
print(marks["sahil"]) #This return error.
