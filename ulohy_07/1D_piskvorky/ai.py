from random import randrange

def tah_pocitace(pole, symbol):
    """Vrátí herní pole se zaznamenaným tahem počítače"""
    while True:
        # Náhodně vybere pozici od 0 do 19
        pozice = randrange(19)
        # Ošetření, že nemůže zadat na obsazenou pozici
        if pole[pozice] == "-":
            break
        else:
            raise RuntimeError("Na této pozici již herní znak je.")

    vysledek_pocitac = pole[:pozice] + symbol + pole[pozice + 1:]
   
    return vysledek_pocitac
    