# f = open("poem.txt")
# print(f.read())
# f.close

with open("poem.txt") as f:
    content = f.read()

    if "twinkle" in content:
        print("The word twinkle is present")
    else:
        print("The word twinkle is not present")

    print(content)
