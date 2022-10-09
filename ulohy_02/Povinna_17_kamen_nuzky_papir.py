from random import randrange

gamer  = input("Kámen, nůžky nebo papír? ")
comp = randrange(3)

if gamer == "kámen" or "Kámen":
    gamer = 0
elif gamer == "nůžky" or "Nůžky":
    gamer = 1
elif gamer == "papír" or "Papír":
    gamer = 2
else:
    print("Toto je špatné zadání")

if (gamer == 0 and comp == 1) or (gamer == 1 and comp == 2) or (gamer == 2 and comp == 0):
    print("Vyhráváš :-)")
elif (gamer == 0 and comp == 2) or (gamer == 1 and comp == 0) or (gamer == 2 and comp == 1):
    print("Vyhrává počítač :-(")
else:
    print("Plichta")