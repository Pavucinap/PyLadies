animals = ["pes", "kočka", "had"]
# print(animals) #vypíše i s hranatou závorkou

for a in animals:
    print(a)  # vypíše je pod sebe jednotlivě

animals.append("cat") 
animals.append(10) # přidá prvek na konec, nemusí být stejný datový typ
print(animals)

animals.remove(10) # neudává se index, ale hodnota, kterou chci vymazat

len(animals) # kolik prvků

animals.count("kočka") # když je víckrát, spočítá, kolikrát

animals.sort() # nenávratně poskládá dle abecedy či od nejmenšího

animals.index("kočka") # na kolikáté pozici

animals.pop() # vyjme a vypíše poslední hodnotu

animals.reverse() # otočí seřazení původního (není opak sort)

animals[1] # zobrazí prvek na pozici (dá se i více, stejně jak u stringů)

animals[1] = "papoušek" # přepíše prvek na pozici

wild_animals = ["lev", "tygr", "liška", "sova"]
all_animals = []
all_animals.extended(wild_animals)
all_animals.extend(animals)

# nebo

all_animals = animals + wild_animals #stejně jako když vložím jedny i druhé

all_animals = animals + wild_animals * 3 # divoká budou 3x za sebou

if all_animals: #tento zápis je if True
    print("Seznam není prázdný")
# zjednodušeně přetypováním
bool(all_animals) # True
bool([]) # False


pozdrav = "Ahoj!"
list(pozdrav) # vypíše na jednotlivá písmena


x = "Ahoj, ahoj, to je super."
x.split(",") # rozdělí na jednotlivé prvky podle toho, co je v závorce definované

# Opak metoda stringu join
",".join(wild_animals) # první podle čeho spojit, pak join a do závorky co

all = [animals, wild_animals, [1, 5, 6]]
print(all)
# vypíše se seznam složený ze seznamů [['kočka', 'papoušek', 'had'], ['lev', 'tygr', 'liška', 'sova'], [1, 5, 6]]
all[1][-1][:2] # vypíše od 3. písmene posledního prvku prvního seznamu