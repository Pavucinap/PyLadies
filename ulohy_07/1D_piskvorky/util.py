def tah(pole, symbol, zvolena_pozice):
    """Vrátí herní pole se zaznamenaným tahem hráče"""
    if not 0 <= zvolena_pozice < len(pole):
        raise IndexError("Pozice je mimo rozsah herního pole. Zvol prosím pozici 0 - 19.")
    # Ošetření, že se nezapíše znak na pozici, kde již nějaký je
    elif pole[zvolena_pozice] != "-":
        raise RuntimeError("Na této pozici již herní znak je. Zvol jinou.")
    else:
        vysledek = pole[:zvolena_pozice] + symbol + pole[zvolena_pozice + 1:]
   
    return vysledek