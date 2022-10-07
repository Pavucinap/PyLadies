a = str(input("Zadej první číslo: "))
b = str(input("Zadej druhé číslo: "))
o = str(input("Zadej matematickou operaci (+, -, *, /): "))

if o == ["+", "-", "*", "/"] and a.isdigit() and b.isdigit():
    r = a + o + b
    print("{} {} {} = {}".format(a, o, b, eval(r)))     # eval - vyhodnoť co je uvedeno v závorce
else:
    print("Toto není správné zadání!")