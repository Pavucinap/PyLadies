from class_currency import Currency
from class_invoice import Invoice
from util import numeric_check, currency_check, CurrencyError
import datetime
import json


Currency.get_json_to_file()

print("Generátor faktur.")
print("Částka v jiných měnách než Kč, bude převedena dle platného kurzu ČNB.")

while True:
    product = input("O jaký produkt se jedná? ")
    if product != "":
        break
    else:
        print("Musí být zadán název produktu.")

while True:
    amount = input("Jaké je množství? ")
    if numeric_check(amount):
        amount = float(amount)
        break
    else:
        print("Musí být zadáno kladné číslo.")

while True:
    unit_price = input("Jaká je jendotková cena? ")
    if numeric_check(unit_price):
        unit_price = float(unit_price)
        break
    else:
        print("Musí být zadáno kladné číslo.")

while True:
    currency = input("Jaká je měna? ").upper()
    if currency in ['KC', 'KČ', 'CZK']:
        unit_price_CZK = unit_price
        break
    elif currency_check(currency):
        with open(f"currency-{str(datetime.date.today())}.txt") as f:
            rates = json.loads(f.read())
            unit_price_CZK = unit_price * rates['kurzy'][currency]['dev_stred']
        break
    else:
        raise CurrencyError("S touto měnou není možné počítat.")

print("Generuji fakturu...")

inv = Invoice(unit_price_CZK, currency, product, amount)
inv.generate_invoice()

print(f'Faktura je hotová na odkaze <"Faktury/Faktura_{inv.symbol}.html">')
