print('Odpovídej "ano" nebo "ne".')

stastna = input("Jsi šťastná? ")
bohata = input("Jsi bohatá? ")

if stastna == "ano" or stastna == "Ano":
    if bohata == "ano" or bohata == "Ano":
        print("Gratuluji, jsi šťastná žena.")
    elif bohata == "ne" or bohata == "Ne":
        print("Tak zkus méně utrácet nebo si najdi lepší práci. :-)")
    else:
        print("Toto je špatné zadání")

elif stastna == "ne" or stastna == "Ne":
    if bohata == "ano" or bohata == "Ano":
        print("Tak alespoň něco. Zkus se víc usmívat.")
    elif bohata == "ne" or bohata == "Ne":
        print("Tak zkus méně utrácet nebo si najdi lepší práci. :-)")
    else:
        print("Toto je špatné zadání")

else:
    print("Toto je špatné zadání")