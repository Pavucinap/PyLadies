from random import randrange

sum = 0

for _ in range(2):
    sum = sum + randrange(2,10)

print("Součet rozdaných karet je:", sum)

while True:
    answer = input("Chcete další kartu? Ano/Ne ")
    if answer == "Ne" or answer == "ne":
        break
    if answer == "Ano" or answer == "ano":
        card = randrange(2,10)
        print("Další karta je:", card)
        sum = sum + card
        print("Součet karet je:", sum)
        if sum >= 21:
            break

if sum < 21:
    print("Výborně, ale do 21 chybí", 21 - sum, "bodů.")
elif sum == 21:
    print("Skvělé. Oko bere!")
else:
    print("Bohužel, to už je moc. Prohráváš.")