word = input("Zadej slovo či sloví spojení: ")

print("Počet znaků ve slově či slovním spojení:", len(word))

while True:
    pos = int(input("Kolikátý znak chceš nahradit? "))
    if pos <= len(word):
        break
    print("Bohužel tolik znaků nemáme k dispozici. :-)")

change = input("Za co se má zvolený znak zaměnit: ")
print("Původní slovo či slovní spojení se mění na: " + word[:pos-1] + change + word[pos:])