import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == "r":
        if you == "s":
            return False
        elif you == "p":
            return True 
    elif comp == "p":
        if you == "r":
            return False
        elif you == "s":
            return True 
    elif comp == "s":
        if you == "p":
            return False
        elif you == "r":
            return True 

print("Computer's Turn : Rock(r) Paper(p) or Sissors(s)?")
randno = random.randint(1, 3)
if randno == 1:
    comp = "r"
elif randno == 2:
    comp = "p"
elif randno == 3:
    comp = "s"


you = input(("Your Turn : Rock(r) Paper(p) or Sissors(s)?"))

print(f"Computer Chose {comp}")
print(f"You Chose {you}")

a = gameWin(comp, you)

if comp == you:
    print("This is a tie")
elif a:
    print("You Win")
else:
    print("You Lose") 