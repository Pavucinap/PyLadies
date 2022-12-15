import datetime
import sys
import os
import requests
import json

URL_API = "https://data.kurzy.cz/json/meny/b[6].jso"
# Vím, že odkaz má končit .json, ale tam jsou stará data, tady jsou aktuální. :-)
TODAY = str(datetime.date.today())


class Currency:
    @staticmethod
    def get_json_from_url(url=URL_API):
        """Download json from kurzy.cz according to ČNB."""
        page = requests.get(url)
        page.raise_for_status()
        rates = page.json()
        return rates

    @staticmethod
    def create_file():
        """Creating a file with date in the name if it doesn't exist."""
        try:
            file = open(f"currency-{TODAY}.txt", "w")
            return file
        except IOError:
            sys.exit("Something went wrong!")

    @staticmethod
    def remove_old_files():
        """The old file will be removed if it is in the folder."""
        for file in os.listdir():
            if (file.startswith("currency-")) and file[9:19] != TODAY:
                os.remove(file)

    @staticmethod
    def get_json_to_file():
        """Insert actual data from json to txt file."""
        Currency.remove_old_files()
        if not os.path.isfile(f"currency-{TODAY}.txt"):
            Currency.create_file()
            with open(f"currency-{TODAY}.txt", "w") as f:
                json.dump(Currency.get_json_from_url(), f, ensure_ascii=True,
                          indent=2)
