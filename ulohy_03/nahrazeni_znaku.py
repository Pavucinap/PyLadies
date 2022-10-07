word = input("Zadej slovo či sloví spojení: ")

print("Počet znaků ve slově či slovním spojení:", len(word))

pos = int(input("Kolikátý znak chceš nahradit? "))

while True:
    if pos <= len(word):
        break
    print("Bohužel tolik znaků nemáme k dispozici. :-)")
    pos = int(input("Kolikátý znak chceš nahradit? "))

change = input("Za co se má zvolený znak zaměnit: ")
print("Původní slovo či slovní spojení se mění na: " + word[:pos-1] + change + word[pos:])