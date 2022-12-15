from class_currency import Currency
import datetime
import json


class CurrencyError(Exception):
    """Custom exception . CurrencyError"""
    pass

def currency_check(input_currency):
    """Verification that the currency is in conversion file."""
    with open(f"currency-{str(datetime.date.today())}.txt") as f:
        rates = json.loads(f.read())
        if input_currency in rates["kurzy"]:
            return True
        else:
            return False

def numeric_check(input_number):
    """Verification that a number is entered."""
    try:
        if float(input_number) > 0:
            return True
        else:
            return False
    except ValueError:
        return False
