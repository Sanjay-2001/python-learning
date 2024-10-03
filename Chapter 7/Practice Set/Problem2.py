l = ["Harry", "Soham", "Sachin", "Rahul"]

for i in l:
    if (i.startswith("S")):
        print(f"Hello {i}")

print("------------")
i = 0

while (i < len(l)):
    if (l[i].startswith("S")):
        print(f"welcome {l[i]}")
    i += 1
