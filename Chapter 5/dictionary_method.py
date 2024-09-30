marks = {
    "Sanjay" :100,
    "Akash" : 95,
    "Yash" :90,
    "List":["Sci","Math","Geog"]
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Sanjay" : 80})

print(marks)

print(marks.get("Harry")) #prints none
#print(marks["Harry"]) #returns an errors