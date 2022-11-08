import ai
import util


def tah_hrac(pole, symbol):
    """Vrátí herní pole se zaznamenaným tahem hráče"""
    while True:
        zvolena_pozice = input("Zadej pozici, kam chceš umístit znak (0-19): ")
        # Ošetření, že nezadá písmeno
        if not zvolena_pozice.isdigit():
            print("Zvolená pozice musí být číslo.")
            continue

        zvolena_pozice = int(zvolena_pozice)
        break

    return util.tah(pole, symbol, zvolena_pozice)


def vyhodnot(pole):
    if "xxx" in pole:
        # Vyhrává x
        vyhodnoceni = "x"
    elif "ooo" in pole:
        # Vyhrává o
        vyhodnoceni = "o"
    elif "-" not in pole:
        # Remíza
        vyhodnoceni = "!"
    else:
        # Hra pokračuje
        vyhodnoceni = "-"

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
        hraci_pole = ai.tah_pocitace(hraci_pole, symbol_pc)
        print(f"Tah počítače: \t{hraci_pole}\n")
        # Vyhodnocení tahu počítače
        vyhodnoceni = vyhodnot(hraci_pole)
        # Pokud vyjde něco jiného než konec, pokračujeme
        if vyhodnoceni != "-":
            break

    return vyhodnoceni


def hra():
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
