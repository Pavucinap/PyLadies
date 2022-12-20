import datetime
import os
import sys
from class_qrcodegenerator import QrCodeGenerator


class Invoice:
    def __init__(self, unit_price, currency, product, amount,
                 path=os.getcwd()):
        self.currency = currency
        self.unit_price = unit_price
        self.amount = amount
        self.product = product
        self.path = path
        self.symbol = self.generate_variable_symbol()
        self.account = "2600702427/6800"
        self.iban = "CZ1168000000002600702427"

    def generate_variable_symbol(self):
        """Generate a unique variable symbol"""
        try:
            f = open(f"VS.txt", "r+")
            content = str(int(f.read()) + 1)
            f.seek(0)
            f.write(content)
            f.close()
            return content
        except IOError:
            f = open(f"VS.txt", "w")
            f.write("2022000001")
            f.close()
            return "2022000001"

    def price(self):
        return self.unit_price * self.amount

    def generate_invoice(self):
        """Import data into the invoice template."""
        os.makedirs(self.path, exist_ok=True)
        with open("Faktury/template/template.html", "r",
                  encoding='utf-8') as file:
            QrCodeGenerator.get_qr(self.iban, self.price(), self.symbol)
            text = file.read()
            html_content = text.format(
                invoice_number=self.symbol,
                account=self.account,
                invoice_date=datetime.date.today().strftime("%d. %m. %Y"),
                due_date=(datetime.date.today() +
                          datetime.timedelta(days=14)).strftime("%d. %m. %Y"),
                symbol=self.symbol,
                product=self.product,
                quantity=f"{self.amount: .2f}",
                price_per_unit=f"{self.unit_price: .2f}",
                product_price=f"{self.price(): .2f}",
                QRCode=f"QR_Code_{self.symbol}.png"
            )

        with open(f"Faktury/Faktura_{self.symbol}.html", "w",
                  encoding='utf-8') as file_invoice:
            file_invoice.write(html_content)
