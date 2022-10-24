while True:
    r_c = input("Jaké je tvé rodné číslo včetně lomítka? ")
    pred = r_c[0:6] # 6 čísel před lomítkem
    za = r_c[7:11]  # 4 čísla za lomítkem

    # Ošetření správného formátu
    if not (pred.isdigit() and za.isdigit() 
            and len(r_c) == 11 and r_c[6] == "/"):
        print("Toto není správný formát. Zkus to znovu.")
        continue
    
    cislo = pred + za       # složení rodného čísla bez lomítka

    # Zjištění, zda je rodné číslo správně
    # Ověření dělitelnosti 11
    if int(cislo) % 11 != 0:
       print("Toto asi nebude správně. Rodné číslo má být dělitelné 11.")
       continue

    # Pro zjednodušení převod str na int a rozdělení na dvojčíslí
    rok = int(cislo[0:2])
    mes = int(cislo[2:4])
    den = int(cislo[4:6])

    # Pouze pro roky 1985 - 2022
    if 22 < rok <85:
        print("Rok tvého narození není v rozmezí 1985 - 2022")
        continue
    
    # Ošetření čísla měsíce a ženského rodného čísla
    if 50 < mes <=62:
        mes = mes - 50

    if mes > 12:
        print("Nemá rok pouze 12 měsíců?")
        continue
    
    if mes == 0:
        print("Neexistuje měsíc s číslem 0.")
        continue
    
    # Ošetření počtu dnů podle měsíců
    dlouhe = [1, 3, 5, 7, 8, 10, 12]
    kratke = [4, 6, 9, 11]
    if mes in dlouhe and den > 31:
        print("Tolik dnů určitě tvůj měsíc narození nemá.")
        continue
    elif mes in kratke and den > 30:
        print("Tolik dnů určitě tvůj měsíc narození nemá.")
        continue
    elif mes == 2 and rok % 4 == 0 and den > 29:
        print("Tolik dnů určitě tvůj měsíc narození nemá.")
        continue
    elif mes == 2 and rok % 4 != 0 and den > 28:
        print("Tolik dnů určitě tvůj měsíc narození nemá.")
        continue
    elif den == 0:
        print("Neexistuje den s číslem 0.")
        continue

    print(f"Děkuji za zadání správného rodného čísla: {r_c}")
    break
