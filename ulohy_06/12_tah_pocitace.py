# Napiš funkci tah_pocitace, která dostane řetězec s herním polem, 
# vybere pozici, na kterou hrát, a vrátí herní pole se zaznamenaným 
# tahem počítače. Použij jednoduchou náhodnou „strategii”:
    # 1. Vyber číslo od 0 do 19.
    # 2. Pokud je dané políčko volné, hrej na něj.
    # 3. Pokud ne, opakuj od bodu 1.
# Hlavička funkce by tedy měla vypadat nějak takhle:
    # def tah_pocitace(pole):
    # "Vrátí herní pole se zaznamenaným tahem počítače"

from random import randrange

def tah_pocitace(pole = 20 * "-"):
    """Vrátí herní pole se zaznamenaným tahem počítače"""
    while True:
        pozice = randrange(19)
        if pole[pozice] == "-":
            break
    symbol = "o"
    vysledek = pole[:pozice] + symbol + pole[pozice + 1:]
   
    return vysledek

print(tah_pocitace())
