a = int(input("Enter a number: "))
b = int(input("Enter a second number"))

if (b == 0):
    raise ZeroDivisionError("Hey you cannot divide by zero")
else:
    print(f"The divison of number 1 / number 2 is {a/b}")

print("Thank you")
