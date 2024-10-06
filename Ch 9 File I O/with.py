f = open("file.txt")
print(f.read())
f.close()

print("------")

# the same can be written as below using with
with open("file.txt") as f:
    print(f.read())
