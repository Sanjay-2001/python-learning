name_list = ["Sanjay", "Akash", "Yash"]

name = input("Enter your name : ")

if (name.capitalize() in name_list):
    print("Your name is in the list")
else:
    print("Your name is not in the list")
