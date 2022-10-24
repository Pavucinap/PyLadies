zvirata = ["pes", "kočka", "králík", "had"]
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
seznam_zvirat = list(sort_value.values())
print(seznam_zvirat)

# Než jsem si přečetla pořádně zadání, že to má být přes slovníky, tak jsem 
# vytvořila toto a také fungovalo, ale pak jsem předělala podle zadání:

#for zvire in zvirata:
#    zvirata.sort(key=lambda zvire: zvire[1])
#print(f"Zvířata seřazena dle druhého písmene: {zvirata}")

# lambda se používá, když parametr klíče má být funkce (nebo jiná volatelná), 
# která převezme jeden argument a vrátí klíč k použití pro účely řazení
