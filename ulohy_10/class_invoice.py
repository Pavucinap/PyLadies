import datetime
import os
from class_qrcodegenerator import QrCodeGenerator

ACCOUNT = "2600702427/6800"
IBAN = "CZ1168000000002600702427"


class Invoice:
    def __init__(self, unit_price, currency, product, amount,
                 path=os.getcwd()):
        self.currency = currency
        self.unit_price = unit_price
        self.amount = amount
        self.product = product
        self.path = path
        self.symbol = self.generator_variable_symbol()
        try:
            os.makedirs(self.path + "/Faktury")
        except FileExistsError:
            pass

    def generator_variable_symbol(self):
        """Generate a unique variable symbol"""
        with open("VS.txt", "r+") as f:
            content = f.read()
            f.seek(0)
            f.write(str(int(content) + 1))
        with open("VS.txt", "r+") as f_2:
            symbol = f_2.read()
            return symbol

    def price(self):
        return self.unit_price * self.amount

    def generate_invoice(self):
        """Import data into the invoice template."""
        with open("Faktury/template/template.html", "r",
                  encoding='utf-8') as file:
            QrCodeGenerator.get_qr(IBAN, self.price(), self.symbol)
            text = file.read()
            html_content = text.format(
                invoice_number=self.symbol,
                account=ACCOUNT,
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
