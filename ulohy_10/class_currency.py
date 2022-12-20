import datetime
import sys
import os
import requests
import json
from exceptions import CurrencyError




class Currency:
    def __init__(self, currency_input, unit_price_input):
        self.url = "https://data.kurzy.cz/json/meny/b[6].jso"
        self.today = str(datetime.date.today())
        self.currency = currency_input
        self.unit_price = unit_price_input

    def get_json_from_url(self):
        """Download json from kurzy.cz according to ČNB."""
        page = requests.get(self.url)
        page.raise_for_status()
        rates = page.json()
        return rates

    def create_file(self):
        """Creating a file with date in the name if it doesn't exist."""
        try:
            file = open(f"currency-{self.today}.txt", "w")
            return file
        except IOError:
            sys.exit("Something went wrong!")

    def remove_old_files(self):
        """The old file will be removed if it is in the folder."""
        for file in os.listdir():
            if (file.startswith("currency-")) and file[9:19] != self.today:
                os.remove(file)

    def get_json_to_file(self):
        """Insert actual data from json to txt file."""
        self.remove_old_files()
        if not os.path.isfile(f"currency-{self.today}.txt"):
            self.create_file()
            with open(f"currency-{self.today}.txt", "w") as f:
                json.dump(self.get_json_from_url(), f, ensure_ascii=True,
                          indent=2)

    def currency_check(self):
        """Verification that the currency is in conversion file."""
        with open(f"currency-{self.today}.txt") as f:
            rates = json.loads(f.read())
            return self.currency in rates["kurzy"]

    def calculate_unit_price (self):
        if self.currency in ['KC', 'KČ', 'CZK']:
            return self.unit_price
        elif self.currency_check():
            with open(f"currency-{self.today}.txt") as f:
                rates = json.loads(f.read())
            return (self.unit_price / rates['kurzy'][self.currency]['jednotka'])\
                    * rates['kurzy'][self.currency]['dev_stred']
        else:
            raise CurrencyError("S touto měnou není možné počítat.")

    def convert(self):
        self.get_json_to_file()
        return self.calculate_unit_price()
