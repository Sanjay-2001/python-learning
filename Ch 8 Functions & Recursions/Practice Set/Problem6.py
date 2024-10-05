def rem(l, word):
    n = []
    for item in l:
        if not (item == word):
            # n.append(item.strip(word))
            n.append(item.replace(word, ""))
    return n


l = ["Sunday", "Monday", "Tuesday", "January", "February", "March"]

print(rem(l, "day"))
