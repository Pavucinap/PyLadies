class Interfacings:
    def __init__(self, interfacing_type):
        self.interfacing_type = interfacing_type

    def price(self):
        """Ošetření, že bude zadáno pouze číslo."""
        while True:
            try:
                price = float(input("\nKolik korun stojí bm výztuhy? "))
                if price < 0:
                    print("Cena nemůže být záporné číslo.")
                    continue
            except ValueError:
                print("Cena není číslo nebo je desetinná čárka místo tečky.")
                continue
            else:
                return price

    def interfacing_width(self):
        """Ošetření zadání šíře, nutné pro výpočet ceny za m2."""
        while True:
            try:
                width = int(input("Jaká byla šíře výztuhy v cm? ")) / 100
                if width <= 0:
                    print("Šíře nemůže být záporné číslo nebo 0.")
                    continue
            except ValueError:
                print("Šíře nebyla zadána správně. Zadávej v cm.")
                continue
            else:
                return width

    def interfacing_price(self):
        """Výpočet ceny množství potřebného pro ušití"""
        used = 0.62
        price = self.price() / self.interfacing_width() * used
        return price
