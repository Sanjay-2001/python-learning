from random import randint

computer = randint(1, 100)

print("❇️Enter a number between 1️, 100❇️\n")

i = 1

with open("score.txt") as f:
    score = f.read()


while (True):
    userInput = int(input("Enter number 😊: "))
    if (computer > userInput):
        print("Hint: Use Higher Number ⬆️\n")
    elif (computer < userInput):
        print("Hint: Use Lower Number ⬇️\n")
    else:
        print(f"""
              🥳Congrats🥳
              You guessed the correct number : {computer}
              The number of guesses {i} 🤩
              """)
        if (score == ""):
            with open("score.txt", "w")as f:
                f.write(str(i))
        elif (int(score) > i):
            print(
                f"Previous record broken : {int(score)} guesses.\nNew record 😎 :{i} guesses\n")
            with open("score.txt", "w")as f:
                f.write(str(i))
        else:
            print(f"Previous record not broken 😢 {int(score)} guesses\n")
        break
    i += 1
