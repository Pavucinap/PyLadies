from random import randrange

def tah_hrac(pole, symbol):
    """Vrátí herní pole se zaznamenaným tahem hráče"""
    while True:
        zvolena_pozice = input("Zadej pozici, kam chceš umístit znak (0-19): ")
        # Ošetření, že nezadá písmeno
        if not zvolena_pozice.isdigit():
            print("Zvolená pozice musí být číslo.")
            continue

        zvolena_pozice = int(zvolena_pozice)
                    
        # Ošetření správnosti rozsahu pozice
        if not 0 <= zvolena_pozice <= len(pole):
            print("Pozice je mimo rozsah herního pole. Zvol prosím pozici 0 - 19.")
            continue
        # Ošetření, že se nezapíše znak na pozici, kde již nějaký je
        elif pole[zvolena_pozice] != "-":
            print("Na této pozici již herní znak je. Zvol jinou.")
            continue

        break

    vysledek_hrac = pole[:zvolena_pozice] + symbol + pole[zvolena_pozice + 1:]
   
    return vysledek_hrac

def tah_pocitace(pole, symbol):
    """Vrátí herní pole se zaznamenaným tahem počítače"""
    while True:
        # Náhodně vybere pozici od 0 do 19
        pozice = randrange(19)
        # Ošetření, že nemůže zadat na obsazenou pozici
        if pole[pozice] != "-":
            continue

        break

    vysledek_pocitac = pole[:pozice] + symbol + pole[pozice + 1:]
   
    return vysledek_pocitac

def vyhodnot(pole):
    if "xxx" in pole:
        vyhodnoceni = "x" # Vyhrává x
    elif "ooo" in pole:
        vyhodnoceni = "o" # Vyhrává o
    elif "-" not in pole:
        vyhodnoceni = "!" # Remíza
    else:
        vyhodnoceni = "-" # Hra pokračuje
    
    return vyhodnoceni

def piskvorky1d(symbol_hr, symbol_pc):
    hraci_pole = 20 * "-"
    
    while True:
        # Volání a vypsání tahu hráče
        hraci_pole = tah_hrac(hraci_pole, symbol_hr)
        print(f"Tah hráče: \t{hraci_pole}")
        # Vyhodnocení tahu hráče
        vyhodnoceni = vyhodnot(hraci_pole)
        # Pokud vyjde něco jiného než konec, pokračujeme
        if vyhodnoceni != "-":
            break
        # Volání a vypsání tahu počítače
        hraci_pole = tah_pocitace(hraci_pole, symbol_pc)
        print(f"Tah počítače: \t{hraci_pole}\n")
        # Vyhodnocení tahu počítače
        vyhodnoceni = vyhodnot(hraci_pole)
        # Pokud vyjde něco jiného než konec, pokračujeme
        if vyhodnoceni != "-":
            break
    
    return vyhodnoceni

# Hráč si  zvolí svůj symbol, volí jen 1x, proto globální proměnná
while True:
    symbol_hrac = input("Jaký je tvůj znak ve hře, 'x' nebo 'o'? ")
    # ošetření, aby zvolil jen "x" nebo "o"
    if symbol_hrac not in ("x", "o"):
        print("Herní symboly jsou pouze 'x' nebo 'o'")
        continue
    
    break

# Přiřazení symbolu počítači podle volby  hráče
if symbol_hrac == "o":
    symbol_pocitac = "x"
else:
    symbol_pocitac = "o"

# Vyhodnocení celkového výsledku
vysledek = piskvorky1d(symbol_hrac, symbol_pocitac)

if vysledek == symbol_hrac:
    print("Super, vyhráváš.")
elif vysledek == "!":
    print("Škoda, remíza.")
else:
    print("Bohužel, počítač je chytřejší.")
