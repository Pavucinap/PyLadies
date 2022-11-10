# Napiš funkci tah, která dostane řetězec s herním polem, číslo políčka (0-19),
# a symbol (x nebo o) a vrátí herní pole (t.j. řetězec) s daným symbolem 
# umístěným na danou pozici.
# Hlavička funkce by tedy měla vypadat nějak takhle:
    # def tah(pole, cislo_policka, symbol):
    # "Vrátí herní pole s daným symbolem umístěným na danou pozici"

hraci_pole = 20 * "-"
zvolena_pozice = int(input("Zadej pozici, kam chceš umístit znak (0-19): "))
zvoleny_symbol = input("Jaký je tvůj znak ve hře, 'x' nebo 'o'? ")

def tah(pole, pozice, symbol):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici"""
    vysledek = pole[:pozice] + symbol + pole[pozice + 1:]
   
    return vysledek

print(tah(hraci_pole, zvolena_pozice, zvoleny_symbol))
