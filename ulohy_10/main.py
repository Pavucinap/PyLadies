from class_currency import Currency
from class_invoice import Invoice
from util import numeric_check


print("Generátor faktur.")
print("Částka v jiných měnách než Kč, bude převedena dle platného kurzu ČNB.")

while True:
    product = input("O jaký produkt se jedná? ")
    if product != "":
        break
    print("Musí být zadán název produktu.")

while True:
    amount = input("Jaké je množství? ")
    if numeric_check(amount):
        amount = float(amount)
        break
    print("Musí být zadáno kladné číslo.")

while True:
    unit_price = input("Jaká je jendotková cena? ")
    if numeric_check(unit_price):
        unit_price = float(unit_price)
        break
    print("Musí být zadáno kladné číslo.")

currency = input("Jaká je měna? ").upper()
cur = Currency(currency, unit_price)
unit_price_CZK = cur.convert()

print("Generuji fakturu...")

inv = Invoice(unit_price_CZK, currency, product, amount)
inv.generate_invoice()

print(f'Faktura je hotová na odkaze <"Faktury/Faktura_{inv.symbol}.html">')
