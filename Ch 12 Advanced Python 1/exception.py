try:
    a = int(input("Enter a number : "))
    print(a)

except ValueError as v:
    print("Invalid Input :::", v)

except Exception as e:
    print(e)

print("Thank you😊")
