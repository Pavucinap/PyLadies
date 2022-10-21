zvirata = ["pes", "kočka", "králík","had"]
print(f'Všechna: {zvirata}')

# úloha 1 - vypiš všechna zvířata, která jsou kratší než 5 písmen
kratke = []
for zvire in zvirata:
    if len(zvire) <5:
        kratke.append(zvire)
print(f"Kratší než 5 písmen: {kratke}")

# úloha 2 - vypiš všechna zvířata, která začínají na k
zacina = []
for zvire in zvirata:
    if zvire[0] == "k":
        zacina.append(zvire)
print(f"Na písmeno k začíná: {zacina}")

# úloha 3 - zadej slovo a zjisti, zda je ve zvířatech
zadane = input("Jaké zvíře hledáš? ")
if zadane in zvirata:
    print("Ano, je tam.")
else:
    print("Ne, není tam.")

# úloha 4 - oba seznamy, jen v prvním seznamu, jen v druhém seznamu
list1 = ["králík", "pes", "kráva", "prase", "slepice"]
list2 = ["pes", "kočka", "slepice", "koza", "ovce"]

vsechna = list1 + list2
prvni = []
for zvire in list1:
    if zvire not in list2:
        prvni.append(zvire)

druhy = []
for zvire in list2:
    if zvire not in list1:
        druhy.append(zvire)

print(f"Všechna zvířata jsou:{vsechna}")
print(f"Pouze v prvním seznamu jsou: {prvni}")
print(f"Pouze v druhém seznamu jsou: {druhy}")

# úloha 5 - seřazení podle abecedy
zvirata.sort()
print(f"Zvířata seřazena dle abecedy: {zvirata}")

# úloha 6 - seřazení podle 2. písmene
zvirata.append("andulka")

# Slovník ze seznamu, klíč je druhý znak ve slově a hodnota je slovo
zvirata_dict = {}
for zvire in zvirata:
    zvirata_dict[zvire[1]] = zvire

# Seřazení klíčů
keys = zvirata_dict.keys()
sort_letters = sorted(keys)

# Vytvoření nového slovníku dle seřazených klíčů
sort_value = {}
for key in sort_letters:
    sort_value[key] = zvirata_dict[key]

# Vypsání pouze hodnot slovníku jako seznam
seznam_zvirat = list(zvirata_dict.values())
print(seznam_zvirat)

# Než jsem si přečetla pořádně zadání, že to má být přes slovníky, tak jsem 
# vytvořila toto a také fungovalo, ale pak jsem předělala podle zadání:

#for zvire in zvirata:
#    zvirata.sort(key=lambda zvire: zvire[1])
#print(f"Zvířata seřazena dle druhého písmene: {zvirata}")

# lambda se používá, když parametr klíče má být funkce (nebo jiná volatelná), 
# která převezme jeden argument a vrátí klíč k použití pro účely řazení
