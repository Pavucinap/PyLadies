def format(rodne_cislo):
    """Ověří správnost zápisu RRMMDD/XXXX"""
    if (rodne_cislo[0:6].isdigit() and rodne_cislo[7:11].isdigit() 
            and len(rodne_cislo) == 11 and rodne_cislo[6] == "/"):
       return True
    else:
        print("Správný zápis je ve formátu RRMMDD/XXXX")
        return False

def delitelnost(rodne_cislo):
    """Ověří, zda je číslo dělitelné 11"""
    cislo = rodne_cislo[0:6] + rodne_cislo[7:11]
    if int(cislo) % 11 == 0:
       return True
    else:
        print("Rodné číslo musí být dělitelné 11.")
        return False

def datum(rodne_cislo):
    """Zjistí, zda jsou čísla správně a vypíše datum narození."""
    rok = int(rodne_cislo[0:2])
    mes = int(rodne_cislo[2:4])
    den = int(rodne_cislo[4:6])

    if 22 < rok < 85:
        print("Rok se může pohybovat v rozmezí 1985 - 2022.")
        return False
    
    if 0 <= rok <= 22:
        rok = (f"20{rok:02d}") 
    else:
        rok = (f"19{rok:02d}") 

    if 50 < mes <=62:
        mes = mes - 50

    if mes == 00 or mes > 12:
        print("Měsíce se uvádějí ve formátu 01-12 pro muže a 51-62 pro ženy.")
        return False
           
    # Ošetření počtu dnů podle měsíců
    dlouhe = [1, 3, 5, 7, 8, 10, 12]
    kratke = [4, 6, 9, 11]
    if mes in dlouhe and den > 31:
        print(f"{mes}. měsíc má 31 dní.")
        return False
    elif mes in kratke and den > 30:
        print(f"{mes}. měsíc má 30 dní.")
        return False
    elif mes == 2 and int(rok) % 4 == 0 and den > 29:
        print(f"{mes}. měsíc měl v roce {rok} 29 dní.")
        return False
    elif mes == 2 and int(rok) % 4 != 0 and den > 28:
        print(f"{mes}. měsíc měl v roce {rok} 28 dní.")
        return False
    elif den == 0:
        print("Číslo dne nemůže být 0")
        return False

    datum_nar = (f"{den:02d}. {mes:02d}. {rok}")

    return datum_nar

def pohlavi(rodne_cislo):
    """Zjistí pohlaví zadavatele"""
    if 0 < int(rodne_cislo[2:4]) <= 12:
       odpoved = "muž"
    else:
        odpoved = "žena"
    
    return odpoved

def kontrola(rodne_cislo):
    if not format(r_c):
        return False
        
    if not delitelnost(r_c):
        return False
    
    if not datum(r_c):
        return False

    return True
 
while True:
    r_c = input("Jaké je tvé rodné číslo? ")

    if not kontrola(r_c):
        continue
    
    print(f"Datum tvého narození je {datum(r_c)} a jsi {pohlavi(r_c)}.")
    
    break
