def game():
    return 445

score = game()

with open("highscore.txt","r") as f:
    highscorestr = f.read()

if highscorestr=="":
    with open("highscore.txt", "w") as f:
            a = f.write(str(score))
    
elif int(highscorestr) < score:
    with open("highscore.txt", "w") as f:
        a = f.write(str(score))

