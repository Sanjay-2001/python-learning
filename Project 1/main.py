import random
"""
1 for rock
-1 for paper
0 for scissor    
"""

computer = random.choice([-1, 0, 1])

print("""
      r - rock 🪨
      p - paper 📃
      s - scissor ✂️
      """)
youStr = input("Enter your choice: ")

youDict = {"r": 1, "p": -1, "s": 0}
reverseDict = reverseDict = {1: "Rock 🪨", -1: "Paper 📃", 0: "Scissor ✂️"}

if youStr in youDict:
    you = youDict[youStr]

    print(
        f"\nComputer chose {reverseDict[computer]}\nYou chose {reverseDict[you]}")
    print("-----------------------")

    if computer == you:
        print("It's a draw 😒😒😒")
    elif (computer == 1 and you == 0) or (computer == 0 and you == -1) or (computer == -1 and you == 1):
        print("You lose 😂😂😂")
    else:
        print("You win 🤬🤬🤬")
else:
    print("Invalid input! Please enter 'r', 'p', or 's'.")
