if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <=3)")

if (n := len([1, 2, 3])+len([1, 2, 3, 4]) > 5):
    print(f"yes 3+4 is greater than 5")
