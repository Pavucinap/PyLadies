seznam = ["franta vomáčka", "Petr Novák", "Libor levý"]

chybny_zaznam = []
spravny_zaznam = []
opraveny_zaznam = []

for cele_jmeno in seznam:
    jmeno = cele_jmeno.split(" ")
    if jmeno[0][0].islower() or jmeno [1][0].islower():
        chybny_zaznam.append(jmeno)
    if jmeno[0][0].isupper() and jmeno [1][0].isupper():
        spravny_zaznam.append(cele_jmeno)

for name in chybny_zaznam:
    oprava = f"{name[0].capitalize()} {name[1].capitalize()}"
    opraveny_zaznam.append(oprava)
    
print(chybny_zaznam)
print(spravny_zaznam)
print(opraveny_zaznam)
