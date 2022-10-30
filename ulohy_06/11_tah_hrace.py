# Napiš funkci tah_hrace, která dostane řetězec s herním polem, zeptá se hráče,
# na kterou pozici chce hrát, a vrátí herní pole se zaznamenaným tahem hráče.
# Funkce by měla odmítnout záporná nebo příliš velká čísla a tahy na obsazená 
# políčka. Pokud uživatel zadá špatný vstup, funkce mu vynadá a zeptá se znova.


hraci_pole = 20 * "-"

while True:
    zvolena_pozice = input("Zadej pozici, kam chceš umístit znak (0-19): ")
    # Ošetření, že nezadá písmeno
    if not zvolena_pozice.isdigit():
        print("Zvolená pozice musí být číslo.")
        continue
    zvolena_pozice = int(zvolena_pozice)
                
    # Ošetření správnosti rozsahu pozice
    if not 0 <= zvolena_pozice < len(hraci_pole):
        print("Pozice je mimo rozsah herního pole. Zvol prosím pozici 0 - 19.")
        continue
    # Ošetření, že se nezapíše znak na pozici, kde již nějaký je
    elif hraci_pole[zvolena_pozice] != "-":
        print("Na této pozici již herní znak je. Zvol jinou.")
        continue
    break

while True:
    zvoleny_symbol = input("Jaký je tvůj znak ve hře, 'x' nebo 'o'? ")
    if zvoleny_symbol not in ("x", "o"):
        print("Herní symboly jsou pouze 'x' nebo 'o'")
        continue
    break

def tah(pole, pozice, symbol):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici"""
    vysledek = pole[:pozice] + symbol + pole[pozice + 1:]
   
    return vysledek

print(tah(hraci_pole, zvolena_pozice, zvoleny_symbol))
