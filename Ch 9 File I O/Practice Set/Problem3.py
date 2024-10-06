def generateTable(i):
    fileName = f"tables/Table_{i}.txt"

    with open(fileName, "w") as f:
        f.write(f"Table of {i} :\n")

    for j in range(1, 11):
        with open(fileName, "a") as f:
            line = f"{i} X {j} = {i*j} \n"
            f.write(line)


for i in range(2, 5):
    generateTable(i)
