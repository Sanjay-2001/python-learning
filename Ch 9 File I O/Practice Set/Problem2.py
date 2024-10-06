import random


def game():
    print("You are playing the game..")
    score = random.randint(1, 100)
    print(f"Your score : {score}")

    # fetch high score
    with open("score.txt") as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    if (score > hiscore):
        print("new highscore")
        with open("score.txt", "w")as f:
            f.write(str(score))
    else:
        print(f"the high score is still {hiscore}")

    return score


game()
