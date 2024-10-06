st = "Hey I am doing great too"

f = open("myFile.txt", "w")
f.write(st)
f.close()

r = open("myFile.txt")
data = r.read()
print(data)
r.close()


str = """
This is first line
This is second line
This is third line
"""

g = open("file.txt", "w")
g.write(str)
g.close()
