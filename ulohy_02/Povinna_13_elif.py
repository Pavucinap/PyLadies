mira  = int(input("Jakou míru v cm má tebou ulovený pstruh? "))

if mira > 40:
    print("Vážně jsi ulovil pstruha?")
elif mira >= 35:
    print("Tak to už je pořádný kousek. Gratuluji k vzácnému úlovku.")
elif mira >= 30:
    print("Pěkný kousek na filet.")
elif mira >= 25:
    print("Tohoto drobka si již můžeš vzít domů a vleze se ti akorát na pávničku.")
else:
    print("Tohoto drobečka ještě pusť, ještě musí dorůst. Nebo doufej že tě nechytne porybný.")